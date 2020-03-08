class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def figure_field(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)


class Cube:
    def __init__(self, square: Square):
        self.square = square
        self.height = square.height

    def figure_field(self):
        return self.square.figure_field() * 6

    def figure_volume(self):
        return self.square.figure_field() * self.height


class Cuboid:
    def __init__(self, figure, height):
        self.base = figure
        self.height = height

    def figure_field(self):
        return 2 * self.base.figure_field() + 2 * self.base.width + 2 * self.base.height * self.height

    def figure_volume(self):
        return self.base.figure_field() * self.height