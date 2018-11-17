class Human:
    hand = 2
    foot = 2
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def info(self):
        return "My name {}, and my age = {}".format(self.name,self.age)
alex = Human("Alex",12)
olga = Human("Olga",16)
print(alex.info())
print(olga.info())
print(Human.info())
alex.foot=1
alex.child=2
print("child", alex.child)
print("child", olga.child)
print(alex.foot)
print(olga.foot)
print(Human.foot)
Human.foot=3
print(alex.foot)
print(olga.foot)
print(Human.foot)
