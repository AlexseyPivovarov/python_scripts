#с использованием мета-класса мы можем любой класс сделать сингелтоном
#который сохраняет состояние старого объекта в новом
#изменив метод __call__ на return cls._instance = super().__call__(*args, **kwargs)
#его поведение изменится на перезапись старого на новое
class SingletonMeta(type):
    def __init__(cls, *args, **kwargs):
        cls._instance = None
        # cls.get_instance = classmethod(lambda c: c._instance)
        super().__init__(*args, **kwargs)
    def __call__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__call__(*args, **kwargs)
        return cls._instance

class Singleton(metaclass=SingletonMeta):
    def __init__(self, name):
        self._name = name
    def get_name(self):
        return self._name


obj1 = Singleton('MyInstance 1')
# print(obj1())
print (obj1.get_name())  # MyInstance 1

obj2 = Singleton('MyInstance 2')
print (obj2.get_name())  # MyInstance 1

#print (obj1 is obj2 is Singleton.get_instance())
