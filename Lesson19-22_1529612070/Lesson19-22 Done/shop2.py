PAPER = 20


class Product:

    def __init__(self, unit_name="No name", unit_coast=0, unit_weight=0, units="g"):
        self.unit_name = unit_name
        self.unit_coast = unit_coast
        self.unit_weight = unit_weight
        self.units = units


class Buy:

    def __init__(self, product: Product, quantity=1):
        self.quantity = quantity
        self.coast = product.unit_coast * self.quantity
        self.weight = product.unit_weight * self.quantity
        self.unit_name = product.unit_name
        self.unit_coast = product.unit_coast
        self.unit_weight = product.unit_weight
        self.units = product.units


class Check:

    def __init__(self, *args):
        self.buy = args
        self.sum_ = sum((i.coast for i in args))

    def get_info(self):
        print("{:*^{}}".format("Your check", PAPER))
        for item in self.buy:
            space1 = PAPER - len(item.unit_name) - len(str(item.unit_weight)) - len(str(item.unit_coast)) - 2
            space2 = PAPER - len(str(item.quantity)) - len(str(item.weight)) - len(str(item.coast)) - 3
            print("{0} {1}{2:<{4}}${3}\nx{5} {6}{2:<{8}}${7}\n"
                  "".format(item.unit_name, item.unit_weight, item.units, item.unit_coast, space1, item.quantity,
                            item.weight, item.coast, space2))
        space3 = PAPER - len(str(self.sum_)) - 1
        print("{:-<{}}\n{:<{}}${}".format("", PAPER, "SUM:", space3, self.sum_))


if __name__ == '__main__':
    apple = Product("apple", 3, 50)
    fish = Product("fish", 10, 1000)
    milk = Product("milk", 7, 900, "ml")

    firstCheck = Check(Buy(apple, 5), Buy(fish, 2), Buy(milk, 2))
    firstCheck.get_info()


