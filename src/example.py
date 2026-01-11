import numpy as np
import matplotlib.pyplot as plt

from lamina import Lamina
from laminate import Laminate
from beam import EquivalentBeam
from contact import ContactSpring
from solver import ThreePointBendingSolver
from astm_d790 import flexural_modulus, max_flexural_stress
from postprocess import plot_response

# Geometry
L = 0.1
b = 25e-3
h = 0.75e-3

# Material (E-glass/epoxy)
laminas = [
    Lamina(40e9, 10e9, 5e9, 0.25, 0.25e-3, 0),
    Lamina(40e9, 10e9, 5e9, 0.25, 0.25e-3, 90),
    Lamina(40e9, 10e9, 5e9, 0.25, 0.25e-3, 0),
]

laminate = Laminate(laminas)
_, _, D = laminate.ABD()

beam = EquivalentBeam(D11=D[0,0], width=b)
contact = ContactSpring(k=5e3)

solver = ThreePointBendingSolver(beam, contact, span=L)

loads = np.linspace(5, 150, 15)

P1, d1 = solver.solve(loads, include_contact=False)
P2, d2 = solver.solve(loads, include_contact=True)

plot_response(P1, d1, "No contact compliance")
plot_response(P2, d2, "With contact compliance")

plt.legend()
plt.show()

# ASTM properties
Ef = flexural_modulus(P2, d2, L, b, h)
sigma_max = max_flexural_stress(P2.max(), L, b, h)

print(f"Apparent flexural modulus: {Ef/1e9:.2f} GPa")
print(f"Max flexural stress: {sigma_max/1e6:.1f} MPa")
