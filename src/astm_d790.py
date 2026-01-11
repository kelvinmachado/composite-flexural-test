def flexural_modulus(P, delta, L, b, h):
    """
    Secant modulus using initial linear region
    """
    slope = P[1] / delta[1]
    return (L**3 * slope) / (4 * b * h**3)

def max_flexural_stress(Pmax, L, b, h):
    return (3 * Pmax * L) / (2 * b * h**2)
