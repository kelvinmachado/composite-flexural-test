import numpy as np

class Lamina:
    def __init__(self, E1, E2, G12, nu12, t, theta):
        self.E1 = E1
        self.E2 = E2
        self.G12 = G12
        self.nu12 = nu12
        self.nu21 = nu12 * E2 / E1
        self.t = t
        self.theta = np.deg2rad(theta)

    def Q(self):
        denom = 1 - self.nu12 * self.nu21
        Q11 = self.E1 / denom
        Q22 = self.E2 / denom
        Q12 = self.nu12 * self.E2 / denom
        Q66 = self.G12
        return np.array([
            [Q11, Q12, 0],
            [Q12, Q22, 0],
            [0,   0,   Q66]
        ])

    def Qbar(self):
        m = np.cos(self.theta)
        n = np.sin(self.theta)

        T = np.array([
            [ m**2,  n**2,  2*m*n],
            [ n**2,  m**2, -2*m*n],
            [-m*n,   m*n,   m**2 - n**2]
        ])

        Tinv = np.linalg.inv(T)
        return Tinv @ self.Q() @ Tinv.T
