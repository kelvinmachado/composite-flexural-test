import numpy as np

class ThreePointBendingSolver:
    def __init__(self, beam, contact, span):
        self.beam = beam
        self.contact = contact
        self.L = span

    def solve(self, loads, include_contact=True):
        EI = self.beam.flexural_rigidity()

        P = np.array(loads)
        delta_beam = P * self.L**3 / (48 * EI)

        if include_contact:
            delta_contact = 2 * (P / 2) / self.contact.k
        else:
            delta_contact = 0.0

        delta_total = delta_beam + delta_contact
        return P, delta_total
