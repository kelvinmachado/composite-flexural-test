import numpy as np

class Laminate:
    def __init__(self, laminas):
        self.laminas = laminas
        self.z = self._compute_z()

    def _compute_z(self):
        z = [-sum(l.t for l in self.laminas) / 2]
        for lamina in self.laminas:
            z.append(z[-1] + lamina.t)
        return z

    def ABD(self):
        A = np.zeros((3,3))
        B = np.zeros((3,3))
        D = np.zeros((3,3))

        for k, lamina in enumerate(self.laminas):
            z0 = self.z[k]
            z1 = self.z[k+1]
            Qb = lamina.Qbar()

            A += Qb * (z1 - z0)
            B += 0.5 * Qb * (z1**2 - z0**2)
            D += (1/3) * Qb * (z1**3 - z0**3)

        return A, B, D
