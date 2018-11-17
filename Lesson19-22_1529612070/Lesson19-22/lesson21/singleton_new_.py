#реализация с сохранением состояния экземпляра
class SingleTone:
    __instance = None
    def __new__(cls, *args, **kwargs):
        if SingleTone.__instance is None:
            SingleTone.__instance = super().__new__(cls)
            SingleTone.__instance.__val = args[0]
        return SingleTone.__instance
    def __str__(self):
        return str(SingleTone.__instance.__val)

a = SingleTone(10)
b = SingleTone(20)
print(a)
print(b)
print(a is b)

#реализация с перезаписью значения
class SingleToneOnly:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance
    def __init__(self, *args, **kwargs):
        self.a = args[0]
    def __str__(self):
        return str(self.a)
a = SingleToneOnly(10)
b = SingleToneOnly(20)
print(a)
print(b)
