class Point:
    def __init__(self,x=0,y=0):
        print("O,  new Point!!!")
        self.x=x
        self.y=y
    def __str__(self):
        #return "Ok"
        return "x={0} y={1}".format(self.x,self.y)
    def __repr__(self):
        return "x={0} y={1}".format(self.x,self.y)
    def __add__(self,other):
        from math import sqrt
        return sqrt((self.x-other.x)**2+(self.y-other.y)**2)

class Line():
    def __init__(self,*args):
        self.a=Point(args[0],args[1])
        self.b=Point(args[2],args[3])
        print("New Line")
print(Point(0,0)+Point(2,3))
