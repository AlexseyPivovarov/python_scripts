class Digital:
    def __init__(self, int_=0):
        self.__value=int_
    @property
    def bin(self):
        return bin(self.__value)
    @bin.setter
    def bin(self,value):
        self.__value = int(value,2)
    @property
    def int(self):
        return self.__value
    @int.setter
    def int(self,value):
        self.__value = int(value,2)

a = Digital()
a.bin = '100011100101001'
print(a.int)
