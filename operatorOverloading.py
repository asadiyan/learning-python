class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)


point1 = Point(1, 4)
point2 = Point(2, 8)

print(point1 + point2)
print("---------------------------------------------------------")


class Number:

    def __init__(self, x):
        self.x = x

    def __mul__(self, other):
        x = self.x + other.x
        return x


number_a = Number(3)

number_b = Number(4)

print(number_a * number_b)
