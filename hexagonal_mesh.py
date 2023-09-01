class HexagonPattern:
    def __init__(self, x_repeat, y_repeat):
        self.x_repeat = x_repeat
        self.y_repeat = y_repeat

    def display_pattern(self):
        for y in range(self.y_repeat):
            self.display_top_half()
            self.display_bottom_half()

    def display_top_half(self):
        for x in range(self.x_repeat):
            print(r'/ \_', end='')
        print()

    def display_bottom_half(self):
        for x in range(self.x_repeat):
            print(r'\_/ ', end='')
        print()


if __name__ == '__main__':
    X_REPEAT = 20  # How many times to tessellate horizontally.
    Y_REPEAT = 10  # How many times to tessellate vertically.

    hexagon_pattern = HexagonPattern(X_REPEAT, Y_REPEAT)
    hexagon_pattern.display_pattern()
