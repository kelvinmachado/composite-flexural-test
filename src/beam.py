class EquivalentBeam:
    def __init__(self, D11, width):
        self.D11 = D11
        self.width = width

    def flexural_rigidity(self):
        return self.D11 * self.width
