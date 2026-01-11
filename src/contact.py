class ContactSpring:
    def __init__(self, k):
        self.k = k

    def indentation(self, force):
        return force / self.k
