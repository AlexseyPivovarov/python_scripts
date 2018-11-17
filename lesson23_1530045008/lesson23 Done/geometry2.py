from math import sqrt
from itertools import combinations


#  --------------------------------------------------------------------------------------------------------------------
class MetaBuilderLine(type):

    def __call__(cls, *args, **kwargs):
        if len(args) == 4:
            return cls.try_square(*args)
        elif len(args) == 3:
            return cls.try_triangle(*args)
        else:
            raise Exception("Invalid arguments")

    #  -------------------------------------------------------------------------------------------
    @classmethod
    def try_square(mcs, a, b, c, d):
        if (a == c and b == d) or (a == d and b == c):  # two equal points
            return Line(a, b)

        variants = ((b, c, d, a), (a, c, d, b), (a, b, d, c), (a, b, c, d))

        for i in variants:  # one equal point
            if i[3] in (i[0], i[1], i[2]):
                return Triangle(i[0], i[1], i[2], check=False)

        result = []
        for i in variants:   # counter of variants when point of line lie on straight other line
            if mcs.is_one_line(i[0], i[1], i[2]):
                result.append((mcs.longest_line(i[0], i[1], i[2]), i[3]))

        if len(result) == 1:  # point of line lie on straight other line
            return Triangle(result[0][0].a, result[0][0].b, result[0][1], check=False)

        elif len(result) > 1:  # all points lie on one straight line
            # return result[max(enumerate(item[0].get_len() for item in result), key=lambda item: item[1])[0]][0]
            return sorted(result, key=lambda item: item[0].get_len(), reverse=True)[0][0]

        for i in variants:  # ones point of line is inside triangle constructed from the remaining points
            var = ((i[0], i[1]), (i[1], i[2]), (i[2], i[0]))
            res = sum(mcs.formula(j[0], j[1], i[3]) for j in var)
            if res == 3 or res == 0:
                return Triangle(i[0], i[1], i[2], check=False)

        else:
            return Square(a, b, c, d, check=False)

    @staticmethod
    def formula(a, b, x):
        res = ((a.x - x.x) * (b.y - a.y)) - ((b.x - a.x) * (a.y - x.y))
        if res > 0:
            return 1
        elif res < 0:
            return 0
        else:
            raise Exception("Points lie on one straight line. (def formula())")

    #  -------------------------------------------------------------------------------------------
    def try_triangle(self, a, b, c):
        if a == c or b == c:
            return Line(a, b)
        if self.is_one_line(a, b, c):
            return self.longest_line(a, b, c)
        else:
            return Triangle(a, b, c, check=False)

    @staticmethod
    def is_one_line(a, b, c):
        return True if c.x * (b.y - a.y) - c.y * (b.x - a.x) == a.x * b.y - b.x * a.y else False

    @staticmethod
    def longest_line(a, b, c):
        line_list = (Line(a, b), Line(b, c), Line(a, c))
        # return line_list[max(enumerate(i.get_len() for i in line_list), key=lambda item: item[1])[0]]
        return sorted(line_list, key=lambda item: item.get_len())[2]


#  --------------------------------------------------------------------------------------------------------------------
class LineAppBuilder(metaclass=MetaBuilderLine):

    def __init__(self, *args):
        self.args = args


#  --------------------------------------------------------------------------------------------------------------------
class Obj:

    def __init__(self):
        self.color = "white"

    def get_info(self):
        return "The color is {}".format(self.color)

    def set_color(self, color):
        self.color = color


#  --------------------------------------------------------------------------------------------------------------------
class Square(Obj):

    def __init__(self, point_a, point_b, point_c, point_d, check=True):
        super().__init__()
        self.a = point_a
        self.b = point_b
        self.c = point_c
        self.d = point_d
        if check:
            self.check_for_life()

    def check_for_life(self):
        if not isinstance(MetaBuilderLine.try_square(self.a, self.b, self.c, self.d), Square):
            raise Exception("Invalid arguments")

    def get_lines(self):
        ab = Line(self.a, self.b)
        bc = Line(self.b, self.c)
        cd = Line(self.c, self.d)
        ad = Line(self.a, self.d)
        ac = Line(self.a, self.c)
        bd = Line(self.b, self.d)
        return ab, bc, cd, ad, ac, bd

    def get_len(self):
        return tuple((item.get_len() for item in self.get_lines()))

    # (Ya2 - Ya1) * (Xb2 - Xb1) = (Yb2 - Yb1) * (Xa2 - Xa1)
    def get_type(self):
        list_of_lines = sorted(self.get_lines(), key=lambda item: item.get_len())
        lengs = [item.get_len() for item in list_of_lines]
        counter = 0
        for line in combinations(list_of_lines[:4], 2):
            if (line[0].b.y - line[0].a.y) * (line[1].b.x - line[1].a.x) == \
               (line[1].b.y - line[1].a.y) * (line[0].b.x - line[0].a.x):
                counter += 1
        if counter == 1:
            return "trapezium"
        elif counter > 1:
            if lengs[0] == lengs[1] and lengs[0] == lengs[2] and lengs[0] == lengs[3]:
                if lengs[4] == lengs[5]:
                    return "square"
                else:
                    return "rhombus"
            else:
                return "rectangle"
        else:
            return "No type"

    def __eq__(self, other):
        if isinstance(other, Square):
            if self.a in other and self.b in other and self.c in other and self.d in other:
                return True
            else:
                return False
        else:
            raise Exception("Unsupported type for method __eq__!")

    def __contains__(self, item):
        if isinstance(item, Point):
            if self.a == item or self.b == item or self.c == item or self.d == item:
                return True
            else:
                return False
        else:
            raise Exception("Unsupported type for operation! __contains__")

    def get_info(self):
        return "Square(A{};B{};C{};D{}). {}".format(self.a, self.b, self.c, self.d, super().get_info())


#  --------------------------------------------------------------------------------------------------------------------
class Triangle(Obj):

    def __init__(self, point_a, point_b, point_c, check=True):
        super().__init__()
        self.a = point_a
        self.b = point_b
        self.c = point_c
        if check:
            self.check_for_life()

    def check_for_life(self):
        if self.a == self.b == self.c:
            raise Exception("Points are equal. Creating Triangle is impossible!")
        elif MetaBuilderLine.is_one_line(self.a, self.b, self.c):
            raise Exception("All points lie on one straight line. Creating Triangle is impossible!")

    def __eq__(self, other):
        if isinstance(other, Triangle):
            if self.a in other and self.b in other and self.c in other:
                return True
            else:
                return False
        else:
            raise Exception("Unsupported type for method __eq__!")

    def __contains__(self, item):
        if isinstance(item, Point):
            if self.a == item or self.b == item or self.c == item:
                return True
            else:
                return False
        else:
            raise Exception("Unsupported type for operation! __contains__")

    def get_len(self):
        ab = Line(self.a, self.b).get_len()
        bc = Line(self.b, self.c).get_len()
        ac = Line(self.a, self.c).get_len()
        return ab, bc, ac

    def get_type(self):
        lst = self.get_len()
        if lst[0] == lst[1] and lst[0] == lst[2]:
            return "equilateral"
        elif (lst[0] == lst[1] and lst[0] != lst[2]) or \
             (lst[0] == lst[2] and lst[0] != lst[1]) or \
             (lst[1] == lst[2] and lst[1] != lst[0]):
            return "isosceles"
        else:
            return "No type"

    def get_info(self):
        return "Triangle(A{};B{};C{}). {}".format(self.a, self.b, self.c, super().get_info())


#  --------------------------------------------------------------------------------------------------------------------
class Line(Obj):

    def __init__(self, point_a, point_b):
        super().__init__()
        self.a = point_a
        self.b = point_b
        self.check_for_life()

    def check_for_life(self):
        if self.a == self.b:
            raise Exception("Points are equal. Creating Line is impossible!")

    def get_len(self):
        return round(sqrt(((self.b.x - self.a.x) ** 2) + ((self.b.y - self.a.y) ** 2)), 4)

    def __add__(self, other):
        if isinstance(other, Point):
            return LineAppBuilder(self.a, self.b, other)
        elif isinstance(other, Line):
            return LineAppBuilder(self.a, self.b, other.a, other.b)

    def __eq__(self, other):
        if isinstance(other, Line):
            if self.a in other and self.b in other:
                return True
            else:
                return False
        else:
            raise Exception("Unsupported type for method __eq__!")

    def __contains__(self, item):
        if isinstance(item, Point):
            if self.a == item or self.b == item:
                return True
            else:
                return False
        else:
            raise Exception("Unsupported type for operation! __contains__")

    def get_info(self):
        return "Line(A{};B{}). {}".format(self.a, self.b, super().get_info())


#  --------------------------------------------------------------------------------------------------------------------
class Point(Obj):

    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y

    def __str__(self):
        return "({},{})".format(self.x, self.y)

    def __add__(self, other):
        if isinstance(other, int):
            return Point(self.x + other, self.y + other)
        elif isinstance(other, Point):
            if self == other:
                return Point(self.x, self.y)
            else:
                return Line(self, other)
        elif isinstance(other, Line):
            return other + self

    def __radd__(self, other):
        return self.__add__(other)

    def __eq__(self, other):
        if isinstance(other, Point):
            if self.x == other.x and self.y == other.y:
                return True
            else:
                return False
        else:
            raise Exception("Unsupported type for method __eq__!")

    def __contains__(self, item):
        return True if self == item else False

    def get_info(self):
        return "Point({},{}). {}".format(self.x, self.y, super().get_info())


#  --------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    column1, column2, column3, column4 = 50, 40, 60, 10
    len1 = column1 + column2 + column3 + column4 + 5

    def table_out(operation, must, result, check="None"):
        print("¦{:<{}}¦{:<{}}¦{:>{}}¦{:^{}}¦"
              "".format(operation, column1, must, column2, result, column3, check, column4))

    def line(text):
        head = "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|" \
               "".format("Operation", column1, "Must be", column2, "Result", column3, "check", column4)
        print("{1:=^{2}}\n{0}\n{3:=>{2}}".format(head, text, len1, ""))

    def cline():
        print("{:->{}}\n\n\n\n".format("", len1))

    def checker(example, test):
        if isinstance(test, type(example)):
            return str(example == test)
        else:
            return "TypeErr"


    pointA = Point(1, 1)
    test = pointA + 5
    res = Point(6, 6)

    line(" Point & int ")
    table_out("5 + Point(1,1)", "Point(6,6)", test.get_info(), checker(res, test))
    table_out("Point(1,1) + 5", "Point(6,6)", test.get_info(), checker(res, test))
    cline()

    pointB = Point(2, 1)
    test1 = pointA + pointA
    test2 = pointA + pointB
    res = Line(pointA, pointB)

    line(" Point & Point ")
    table_out("Point(1,1) + Point(1,1)", "Point(1,1)", test1.get_info(), checker(pointA, test1))
    table_out("Point(1,1) + Point(2,1)", "Line(A(1,1);B(2,1))", test2.get_info(), checker(Line(pointA, pointB), test2))
    cline()

    lineA = Line(Point(-1, 1), Point(0, 1))
    lineB = Line(Point(-1, 1), Point(1, 1))
    lineC = Line(Point(-1, 1), Point(0, 0))
    test1 = pointA + lineA
    test2 = lineC + pointA

    line(" Point & Line ")
    table_out("Point(1,1) + Line(A(-1,1);B(0,1))", "Line(A(-1,1);B(1,1))",
              test1.get_info(), checker(lineB, test1))
    table_out("Line(A(-1,1);B(0,0)) + Point(1,1)", "Triangle(A(-1,1);B(0,0);C(1,1))",
              test2.get_info(), checker(Triangle(Point(-1, 1), Point(0, 0), Point(1, 1)), test2))
    cline()

    test1 = lineB + lineB
    lineD = Line(Point(1, 1), Point(-1, 1))
    test2 = lineB + lineD

    line(" Line & Line: two equal points ")
    table_out("Line(A(-1,1);B(1,1)) + Line(A(-1,1);B(1,1))", "Line(A(-1,1);B(1,1))",
              test1.get_info(), checker(lineB, test1))
    table_out("Line(A(-1,1);B(1,1)) + Line(A(1,1);B(-1,1))", "Line(A(-1,1);B(1,1))",
              test2.get_info(), checker(lineB, test2))
    cline()

    test = Line(Point(-1, 0), Point(0, 1)) + Line(Point(0, 1), Point(1, 0))

    line(" Line & Line: one equal point ")
    table_out("Line(A(-1,0);B(0,1)) + Line(A(0,1);B(1,0))", "Triangle(A(-1,0);B(0,1);C(1,0))",
              test.get_info(), checker(Triangle(Point(-1, 0), Point(0, 1), Point(1, 0)), test))
    cline()

    test1 = Line(Point(-1, 0), Point(1, 0)) + Line(Point(0, 0), Point(0, 1))
    test2 = Line(Point(-1, 0), Point(1, 0)) + Line(Point(2, 0), Point(2, 1))

    line(" Line & Line: point of line lie on straight other line ")
    table_out("Line(A(-1,0);B(1,0)) + Line(A(0,0);B(0,1))", "Triangle(A(-1,0);B(1,0);C(0,1))",
              test1.get_info(), checker(Triangle(Point(-1, 0), Point(1, 0), Point(0, 1)), test1))
    table_out("Line(A(-1,0);B(1,0)) + Line(A(2,0);B(2,1))", "Triangle(A(-1,0);B(2,0);C(2,1))",
              test2.get_info(), checker(Triangle(Point(-1, 0), Point(2, 0), Point(2, 1)), test2))
    cline()

    test = Line(Point(-2, 2), Point(-1, 1)) + Line(Point(1, -1), Point(2, -2))

    line(" Line & Line: all points lie on one straight line ")
    table_out("Line(A(-2,2);B(-1,1)) + Line(A(1,-1);B(2,-2))", "Line(A(-2,2);B(2,-2))",
              test.get_info(), checker(Line(Point(-2, 2), Point(2, -2)), test))
    cline()

    test = Line(Point(-1, 2), Point(0, 0)) + Line(Point(0, 1), Point(1, 2))

    line(" Line & Line: ones point of line is inside triangle constructed from the remaining points ")
    table_out("Line(A(-1,2);B(0,0)) + Line(A(0,1);B(1,2))", "Triangle(A(-1,2);B(0,0);C(1,2))",
              test.get_info(), checker(Triangle(Point(-1, 2), Point(0, 0), Point(1, 2)), test))
    cline()

    test = Line(Point(-1, 0), Point(0, 1)) + Line(Point(1, 0), Point(0, -1))

    line(" And finally type Square ")
    table_out("Line(A(-1,0);B(0,1)) + Line(A(1,0);B(0,-1))", "Square(A(-1,0);B(0,1);C(1,0);D(0,-1))",
              test.get_info(), checker(Square(Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)), test))
    cline()

    test1 = Triangle(Point(0, 0), Point(4, 0), Point(2, 4)).get_type()
    test2 = Triangle(Point(0, 0), Point(4, 0), Point(2, sqrt(12))).get_type()

    line(" typing of the class Triangle ")
    table_out("Triangle(A(0,0);B(4,0);C(2,4))", "isosceles", test1, checker("isosceles", test1))
    table_out("Triangle(A(0,0);B(4,0);C(2,sqrt(12)))", "equilateral", test2, checker("equilateral", test2))
    cline()

    test1 = Square(Point(0, 0), Point(2, 10), Point(8, 10), Point(10, 0)).get_type()
    test2 = Square(Point(0, 10), Point(0, 0), Point(10, 10), Point(10, 0)).get_type()
    test3 = Square(Point(0, 0), Point(2, sqrt(12)), Point(4, 0), Point(2, -sqrt(12))).get_type()
    test4 = Square(Point(0, 10), Point(0, 0), Point(12, 10), Point(12, 0)).get_type()

    line(" typing of the class Square ")
    table_out("Square(A(0,0);B(2,10);C(8,10);D(10,0))", "trapezium", test1, checker("trapezium", test1))
    table_out("Square(A(0,10);B(0,0);C(10,10);D(10,0))", "square", test2, checker("square", test2))
    table_out("Square(A(0,0);B(2,sqrt(12));C(4,0);D(2,-sqrt(12)))", "rhombus", test3, checker("rhombus", test3))
    table_out("Square(A(0,10);B(0,0);C(12,10);D(12,0))", "rectangle", test4, checker("rectangle", test4))
    cline()
