class RegisterTypeAccount(type):
    __register_type={}
    def __new__(cls,newclass,bases,atrr):
        new = super().__new__(cls,newclass,bases,atrr)
        cls.__register_type[newclass]=new
        return new
    @classmethod
    def get_all_type(cls):
        return tuple(cls.__register_type)
    @classmethod
    def get_type(cls,objtype):
        return cls.__register_type[objtype]
    @classmethod
    def check_type(cls, objtype):
        if  objtype in cls.__register_type:
            return True
        return False


class Bill:
    def __init__(self):
        self.__number = None
        self.__balance = None
    def get_number(self):
        if self.__number is not None:
            return self.__number
        raise Exception("No deposite number")
    def get_balance(self):
        if self.__balance is not None:
            return self.__balance
        raise Exception("No deposite balance")
    def __set_number(self, number):
        self.__number = number
    def __set_balance(self,balance):
        self.__balance = balance
    def get_info(self):
        return self.__number, self.__balance

class Deposite(Bill):
    def __init__(self):
        self.interest = None
        self.prolongation = None
    def set_number(self):
        raise Exception("Not implementation")
    def set_balance(self):
        raise Exception("Not implementation")
    def get_solution(self):
        return "Deposite"

class YearDeposite(Deposite,metaclass=RegisterTypeAccount):
    def set_number(self,number):
        self._Bill__set_number(number)
    def set_balance(self,balance):
        self._Bill__set_balance(balance)

class Credit(Bill, metaclass=RegisterTypeAccount):
    def set_number(self,number):
        self._Bill__set_number(number)
    def set_balance(self,balance):
        self._Bill__set_balance(balance)

class PrototypeAccount:
    def __init__(self,name,ipn):
        self.name = name
        self.ipn = ipn
        self.__accounts={}
    def set_accounts(self,objtype):
        if  RegisterTypeAccount.check_type(objtype):
            self.__accounts[objtype]=RegisterTypeAccount.get_type(objtype)
    def get_all(self):
        for item in self.__accounts:
            yield item


class CreateBill:
    @staticmethod
    def set_params():
        #параметры для создания нового продукта будуь формироваться динамично
        #так как класс RegisterTypeAccount - мета-класс, его экземпляр - это новый класса
        #в нашем случае мы создаем новый класс 'NewCredit'
        return RegisterTypeAccount('NewCredit',(Bill,RegisterTypeAccount),{})
a = CreateBill.set_params()
print(a)
print(RegisterTypeAccount.get_all_type())
