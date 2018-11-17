class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def info(self):
        if self.x==0 and self.y==0:
            return 0
        return self.x,self.y
    def set_color(self, color):
        self.color = color
    def get_color(self):
        if hasattr(self,"color"):
            return self.color
        return None


points=[]
import random as rd
for  x,y in zip((rd.randint(0,4) for i in range(25)),(rd.randint(0,4) for i in range(25))):
    if x and y:
        for point in points:
            if (x,y)==point.info():
                break
        else:
            points.append(Point(x,y))
for point in points:
    print(point.info())
