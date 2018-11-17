class Human:
    __sey = {
        "ukr": "Вітання! Мене звуть {} і мені {} років",
        "rus": "Привет! Меня зовут {} и мне {} лет",
        "eng": "Hello! My name is {} and I'm {} years old",
        "ger": "Hallo! Mein Name ist {} und ich bin {} Jahre alt",
    }

    def __init__(self, name: str, age: int, lang: str="eng"):
        if not(lang in self.__sey):
            raise ValueError("Unimposible value 'lang'. Imposible variants: 'ukr', 'rus', 'eng', 'ger'")
        self.name = name
        self.age = age
        self.lang = lang

    def speak(self):
        print(self.__sey[self.lang].format(self.name, self.age))


if __name__ == '__main__':
    a = Human("Alex", 8, "gir")
    a.speak()

