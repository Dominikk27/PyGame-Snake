class AstarNode:
    def __init__(self, position):
        self.pos = position
        self.g = 0
        self.h = 0
        self.f = 0
        self.parent = None

    def calculate_f(self):
        self.f = self.g + self.h