def equilateral(sides):
    a, b, c = sides

    return triangle(sides) and len(set(sides)) == 1


def isosceles(sides):
    a, b, c = sides
    return triangle(sides) and len(set(sides)) <= 2


def scalene(sides):
    a, b, c = sides
    return triangle(sides) and len(set(sides)) == 3


def triangle(sides):
    sides.sort()
    return not sides[0] + sides[1] < sides[2] and not sides[0] == 0
