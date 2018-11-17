class MyList:
    def __init__(self,l=[]):
        #делает копию контейнера
        self._l=list(l)
    def __repr__(self):
        return repr(self._l)
    def __len__(self):
        return len(self._l)
    #важный метод для контейнера оператор in
    def __contains__(self,value):
        return value in self._l
    def __bool__(self):
        return bool(self._l)
    def add(self,value):
        self._l.append(value)
    #индексирование элементов
    def __setitem__(self,index,value):
        self._l[index]=value
    def __getitem__(self,index):
        if isinstance(index,tuple):
            return [self._l[i] for i in range(index)]
        elif index==Ellipsis:
            #для инкапсуляции собственной коллекции
            return self._l.copy()
        return self._l[index]
    def __iter__(self):
        # for i in self._l:
        #     yield i
        return (i for i in self._l)



a= MyList([1,2,3])
b=iter(a)
print(next(b))
