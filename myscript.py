from geometricalfigures import Square, Rectangle, Cube, Cuboid

square = Square(2)
print(square.figure_field())

rectangle = Rectangle(2, 5)
print(rectangle.figure_field())

cube = Cube(Square(5))
print(cube.figure_field())
print(cube.figure_volume())

cuboid = Cuboid(Rectangle(2, 3), 4)
print(cuboid.figure_field())
print(cuboid.figure_volume())
