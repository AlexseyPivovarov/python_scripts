if __name__ == '__main__':
    column1, column2, column3, column4 = 50, 40, 60, 10
    len1 = column1 + column2 + column3 + column4 + 5

    def table_out(operation, must, result, check="None"):
        print("|{:<{}}|{:<{}}|{:>{}}|{:^{}}|"
              "".format(operation, column1, must, column2, result, column3, check, column4))

    def line(text):
        head = "|{:^{}}|{:^{}}|{:^{}}|{:^{}}|" \
               "".format("Operation", column1, "Must be", column2, "Result", column3, "check", column4)
        print("{1:-^{2}}\n{0}\n{3:->{2}}".format(head, text, len1, ""))

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

    line("Point & int")
    table_out("5 + Point(1,1)", "Point(6,6)", test.get_info(), checker(res, test))
    table_out("Point(1,1) + 5", "Point(6,6)", test.get_info(), checker(res, test))
    cline()

    pointB = Point(2, 1)
    test1 = pointA + pointA
    test2 = pointA + pointB
    res = Line(pointA, pointB)

    line("Point & Point")
    table_out("Point(1,1) + Point(1,1)", "Point(1,1)", test1.get_info(), checker(pointA, test1))
    table_out("Point(1,1) + Point(2,1)", "Line(A(1,1);B(2,1))", test2.get_info(), checker(Line(pointA, pointB), test2))
    cline()

    lineA = Line(Point(-1, 1), Point(0, 1))
    lineB = Line(Point(-1, 1), Point(1, 1))
    lineC = Line(Point(-1, 1), Point(0, 0))
    test1 = pointA + lineA
    test2 = lineC + pointA

    line("Point & Line")
    table_out("Point(1,1) + Line(A(-1,1);B(0,1))", "Line(A(-1,1);B(1,1))",
              test1.get_info(), checker(lineB, test1))
    table_out("Line(A(-1,1);B(0,0)) + Point(1,1)", "Triangle(A(-1,1);B(0,0);C(1,1))",
              test2.get_info(), checker(Triangle(Point(-1, 1), Point(0, 0), Point(1, 1)), test2))
    cline()

    test1 = lineB + lineB
    lineD = Line(Point(1, 1), Point(-1, 1))
    test2 = lineB + lineD

    line("Line & Line: two equal points")
    table_out("Line(A(-1,1);B(1,1)) + Line(A(-1,1);B(1,1))", "Line(A(-1,1);B(1,1))",
              test1.get_info(), checker(lineB, test1))
    table_out("Line(A(-1,1);B(1,1)) + Line(A(1,1);B(-1,1))", "Line(A(-1,1);B(1,1))",
              test2.get_info(), checker(lineB, test2))
    cline()

    test = Line(Point(-1, 0), Point(0, 1)) + Line(Point(0, 1), Point(1, 0))

    line("Line & Line: one equal point")
    table_out("Line(A(-1,0);B(0,1)) + Line(A(0,1);B(1,0))", "Triangle(A(-1,0);B(0,1);C(1,0))",
              test.get_info(), checker(Triangle(Point(-1, 0), Point(0, 1), Point(1, 0)), test))
    cline()

    test1 = Line(Point(-1, 0), Point(1, 0)) + Line(Point(0, 0), Point(0, 1))
    test2 = Line(Point(-1, 0), Point(1, 0)) + Line(Point(2, 0), Point(2, 1))

    line("Line & Line: point of line lie on straight other line")
    table_out("Line(A(-1,0);B(1,0)) + Line(A(0,0);B(0,1))", "Triangle(A(-1,0);B(1,0);C(0,1))",
              test1.get_info(), checker(Triangle(Point(-1, 0), Point(1, 0), Point(0, 1)), test1))
    table_out("Line(A(-1,0);B(1,0)) + Line(A(2,0);B(2,1))", "Triangle(A(-1,0);B(2,0);C(2,1))",
              test2.get_info(), checker(Triangle(Point(-1, 0), Point(2, 0), Point(2, 1)), test2))
    cline()

    test = Line(Point(-2, 2), Point(-1, 1)) + Line(Point(1, -1), Point(2, -2))

    line("Line & Line: all points lie on one straight line")
    table_out("Line(A(-2,2);B(-1,1)) + Line(A(1,-1);B(2,-2))", "Line(A(-2,2);B(2,-2))",
              test.get_info(), checker(Line(Point(-2, 2), Point(2, -2)), test))
    cline()

    test = Line(Point(-1, 2), Point(0, 0)) + Line(Point(0, 1), Point(1, 2))

    line("Line & Line: ones point of line is inside triangle constructed from the remaining points")
    table_out("Line(A(-1,2);B(0,0)) + Line(A(0,1);B(1,2))", "Triangle(A(-1,2);B(0,0);C(1,2))",
              test.get_info(), checker(Triangle(Point(-1, 2), Point(0, 0), Point(1, 2)), test))
    cline()

    test = Line(Point(-1, 0), Point(0, 1)) + Line(Point(1, 0), Point(0, -1))

    line("And finally type Square")
    table_out("Line(A(-1,0);B(0,1)) + Line(A(1,0);B(0,-1))", "Square(A(-1,0);B(0,1);C(1,0);D(0,-1))",
              test.get_info(), checker(Square(Point(-1, 0), Point(0, 1), Point(1, 0), Point(0, -1)), test))
    cline()