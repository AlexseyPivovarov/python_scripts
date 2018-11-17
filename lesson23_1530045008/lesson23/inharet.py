class Unity:
    def __init__(self, life=0,speed=0):
        self.life = life
        self.speed = speed
    def working(self):
        return ">>><<<"
    def go(self):
        return ">>><<<"

class Worker(Unity):
    def __init__(self,life, speed):
        super().__init__(life,speed)
    def working(self):
        pass
    def go(self):
        return self.life*super().go()
class UnityUnity(Unity):
    def __init__(self,a,v,c=9,sdf=123):
        super().__init__(a,v)
        self.prunk = c

a= UnityUnity()
print(a.speed)
