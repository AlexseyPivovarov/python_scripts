class Prototype:
    __drinks = {}

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get(self):
        return Prototype.__drinks

    @classmethod
    def register(self, info, name):
        if info['type'] in Stock.get():

            Prototype.__drinks[name] = info
        else:
            raise NameError

    def unregister(self, name):
        del(Prototype.__drinks[name])

    @classmethod
    def possible(self, data):
        for name, info in Prototype.__drinks.items():
            if data == info:
                return True
        return False

    def __info(self):
        for name, info in Prototype.__drinks.items():
            yield "{} {}".format(name, info)

    def __str__(self):
        return "\n".join(self.__info())


class Stock:
    __res = {
        'cola': 10,
        'fanta': 10,
        'sprite': 10,
        'glass': 10,
        'paper': 30
    }
    __res_info = {
        'cola': 'концентрат колы',
        'fanta': "концентрат фанты",
        'sprite': "концентрат спрайта",
        'glass': "масса стекла для литья тары",
        'paper': "масса бумаги для штампа этикеток"
    }

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    @classmethod
    def get(self):
        return Stock.__res

    @classmethod
    def get_res_info(self):
        return Stock.__res_info

    def possible_type(self, data):
        if Stock.__res[data['type']] - data['q_type'] >= 0:
            return True
        else:
            return False

    def possible_glass(cls, data):
        if Stock.__res['glass'] - data['glass'] >= 0:
            return True
        else:
            return False

    def possible_paper(cls, data):
        if Stock.__res['paper'] - data['paper'] >= 0:
            return True
        else:
            return False

    def subtraction(self, product):
        Stock.__res[product.data['type']] -= product.data['q_type']
        Stock.__res['glass'] -= product.data['glass']
        Stock.__res['paper'] -= product.data['paper']

    @classmethod
    def restore(self, product, count):
        Stock.__res[product.data['type']] += (product.data['q_type'] * count) * 0.8
        Stock.__res['glass'] += (product.data['glass'] * count) * 0.8
        Stock.__res['paper'] += (product.data['paper'] * count) * 0.8

    def __info(self):
        for name, info in Stock.__res.items():
            yield "{} {}".format(name, info)

    def __str__(self):
        return "\n".join(self.__info())


class Product:
    __counter = {}

    def __init__(self, name, data):
        self.name = name
        self.data = data
        Product.__counter[name] = Product.__counter.get(name, 0) + 1

    @classmethod
    def create_info(cls, type, type_quantity, body, glass_quantity, logo, paper_quantity):
        return {
            'type': type,
            'q_type': type_quantity,
            'body': body,
            'glass': glass_quantity,
            'logo': logo,
            'paper': paper_quantity
        }

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return str(self.name)

    @classmethod
    def get(self):
        return Product.__counter

    @classmethod
    def possible(cls, name):
        if name in Product.__counter:
            return True
        else:
            return False

    @classmethod
    def unregister(cls, name):
        del(Product.__counter[name])

    @classmethod
    def subtraction(cls, name, count):
        Product.__counter[name] -= count

    @classmethod
    def is_zero(cls, name):
        if Product.__counter[name] <= 0:
            return True
        else:
            return False

    @staticmethod
    def counter_info():
        for name, info in Product.__counter.items():
            yield "{} - {} шт.".format(name, info)

    @classmethod
    def info(self):
        return "\n".join(self.counter_info())



class Destructor:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance

    def destruct(self, fabric, product, count):
        Product.subtraction(product.name, count)
        if Product.is_zero(product.name):
            Product.unregister(product.name)
            fabric.unregister(product)
        Stock.restore(product, count)




