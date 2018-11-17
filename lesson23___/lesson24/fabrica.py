from lesson23___.lesson24.prototype import Prototype, Product, Stock, Destructor


class Fabric:
    __stock = Stock()
    __prototype = Prototype()
    __destructor = Destructor()

    def __init__(self):
        self.__regedit = set()

    def register(self, obj):
        self.__regedit.add(obj)

    def unregister(self, obj):
        self.__regedit.discard(obj)

    def get_product(self, name):
        for product in self.__regedit:
            if product.name == name:
                return product
        else:
            raise NameError

    def is_name(self, name):
        for item in self.__regedit:
            if item.name == name:
                return True
        else:
            return False

    def get(self):
        return Fabric.__prototype

    def get_stock(self):
        return Fabric.__stock

    def get_destructor(self):
        return Fabric.__destructor

    def destruct(self, name, count):
        if not self.is_name(name):
            raise NameError
        if Product.get()[name] < count:
            raise ValueError
        Fabric.__destructor.destruct(self, self.get_product(name), count)

    def possible(self, name, data):
        for product in self.__regedit:
            if product.name == name and not product.data == data:
                return False
        return True

    def create(self, name, data):
        if not Fabric.__prototype.possible(data):
            raise ValueError
        if not self.possible(name, data):
            raise NameError
        if not self.__stock.possible_type(data):
            raise TypeError
        if not self.__stock.possible_glass(data):
            raise ArithmeticError
        if not self.__stock.possible_paper(data):
            raise SyntaxError
        return Product(name, data)

    def __info(self):
        for product in self.__regedit:
            yield "{} {}".format(product.name, product.data)

    def __str__(self):
        return "\n".join(self.__info())


class FabricApi(Fabric):

    def get_prototypes(self):
        return super().get()  # вывод рецептов

    def get_stock(self):
        return super().get_stock()

    def __str__(self):
        return super().__str__()

    def set_prototype(self, name, type, type_quantity, body, glass_quantity, logo, paper_quantity):
        try:
            Prototype.register(Product.create_info(type, type_quantity, body, glass_quantity, logo, paper_quantity), name)
        except NameError:
            print('На базе нет такого ресурса')
        # добавление нового рецепта

    def set_product(self, name, prototype_name):
        try:
            product = self.create(name, Prototype.get()[prototype_name])
        except NameError:
            print('Имя занято')
        except ValueError:
            print('Рецепт не зарегестрирован')
        except TypeError:
            print('Недостаточно концентрата {}'.format(Prototype.get()[prototype_name]['type']))
        except ArithmeticError:
            print('Недостаточно стекла')
        except SyntaxError:
            print('Недостаточно бумаги')
        else:
            self.get_stock().subtraction(product)
            self.register(product)
            return product
        # создание продукта из списка доступных

    def counter(self):
        return Product.info()
        # сколько было создано продуктов данного типа

    def destruct(self, name, count):
        try:
            super().destruct(name, count)
        except NameError:
            print('Неверное имя для переработки')
        except ValueError:
            print('Неверное число продуктов для удаления')

    def get_res_info(self, name):
        return Stock.get_res_info().get(name, 'такого ресурса нет в базе')


if __name__ == '__main__':
    fabric = FabricApi()
    fabric.set_prototype("prot1", "cola", 5, "1.5L", 2, "Cola", 5)
    fabric.set_prototype('prot2', 'fanta', 5, '1L', 1, 'Fanta', 5)
    fabric.set_prototype('prot3', 'sprite', 5, '2L', 3, 'Sprite', 5)
    print('------------------------список рецептов--------------------------------')
    print(fabric.get_prototypes())
    print('------------------------состояние склада-------------------------------')
    print(fabric.get_stock())
    print('------------------------производство продукции-------------------------')
    fabric.set_product('cola', 'prot1')
    fabric.set_product('fanta', 'prot2')
    fabric.set_product('sprite', 'prot3')
    fabric.set_product('cola', 'prot1')
    fabric.set_product('cola', 'prot2')
    fabric.set_product('cola', 'prot1')
    print('-------------------------список пордукции-------------------------------')
    print(fabric)
    print('-------------------------состояние склда--------------------------------')
    print(fabric.get_stock())
    print('-------------------------количевство продукции--------------------------')
    print(fabric.counter())
    print('-------------------------переработка 2 единиц cola----------------------')
    fabric.destruct('cola', 2)
    print('-------------------------список продукции-------------------------------')
    print(fabric)
    print('-------------------------состояние склада-------------------------------')
    print(fabric.get_stock())
    print('-------------------------количевство продукции--------------------------')
    print(fabric.counter())
    print("-------------------------описание ресурсов------------------------------")
    print(fabric.get_res_info('glass'))
    print(fabric.get_res_info('cola'))
    print(fabric.get_res_info('soda'))

