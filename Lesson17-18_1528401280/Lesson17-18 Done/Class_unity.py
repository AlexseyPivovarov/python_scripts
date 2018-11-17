class Unity:
    def __init__(self, life: str, speed: int):
        self.life = life
        self.speed = speed

    def working(self):
        return "{0}-{0}".format(self.life)

    def go(self):
        return "{0}-{0} ".format(self.life) * self.speed


class Worker(Unity):
    def __init__(self):
        Unity.__init__(self, "tuk", 1)


class Hunter(Unity):
    def __init__(self):
        Unity.__init__(self, "paf", 2)


class Farmer(Unity):
    def __init__(self):
        Unity.__init__(self, "many", 3)


class Tank(Unity):
    def __init__(self):
        Unity.__init__(self, "dr", 5)


if __name__ == '__main__':

    worker = Worker()
    print(worker.working())
    print(worker.go())
    print()

    hunter = Hunter()
    print(hunter.working())
    print(hunter.go())
    print()

    farmer = Farmer()
    print(farmer.working())
    print(farmer.go())
    print()

    tank = Tank()
    print(tank.working())
    print(tank.go())
    print()

