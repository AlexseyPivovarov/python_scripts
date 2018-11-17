class Temperature:
    def __init__(self,c=0):
        self.__c = c
    @property
    def farengeit(self):
        return round((self.__c*1.8+32),2)
    @farengeit.setter
    def farengeit(self,value):
        self.__c = round((value-32)/1.8,2)

    @property
    def celsius(self):
        return self.__c
    @celsius.setter
    def celsius(self,value):
        self.__c = value

t =Temperature()
print(t.farengeit)
t.farengeit = 100
print(t.celsius)
