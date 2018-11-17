class Point:
    def __init__(self,x,y):
        self.__x = x
        self.__y = y
    @property
    def point(self):
        return (self.__x, self.__y)
    @point.setter
    def point(self, *args):
        self.__x=args[0][0]
        self.__y=args[0][1]
    def __add__(self, obj):
        if isinstance(obj,int):
            return Point(self.__x+obj,self.__y+obj)
        elif isinstance(obj, Point):
            return Sector(self,obj)
    def __radd__(self,obj):
        return self.__add__(obj)
    def __iadd__(self,obj):
        return self.__add__(obj)
class Sector:
    def __init__(self,beg,end):
        self.__beg = beg
        self.__end = end
a=Point(9,10)
a.point=24,10
b=Point(10,19)
a+=b
print(a)
