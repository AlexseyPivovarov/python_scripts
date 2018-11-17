
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
    def set_number(self, number):
        self.__number = number
    def set_balance(self,balance):
        self.__balance = balance
    def get_info(self):
        return self.__number, self.__balance

class Deposite(Bill):
    def __init__(self, interest, prolongation):
        self.interest = interest/100
        self.prolongation = prolongation
    def set_balance(self,balance):
        raise Exception("Not implementation")

class YearDeposite(Deposite):
    def __init__(self, interest, prolongation):
        super().__init__(interest, prolongation)
    def set_balance(self,balance):
        self._Bill__set_balance(balance)

class Account:
    def __init__(self,name,ipn):
        self.name = name
        self.ipn = ipn
        self.__accounts=[]
    def set_accounts(self,type):
        self.__acounts.append(с(interest,prolongation))
    def get_all(self):
        for item in self.__accounts:
            yield item
