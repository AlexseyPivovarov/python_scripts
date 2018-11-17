class MyList:
    def __init__(self,l=[]):
        #делает копию контейнера
        self.__l=list(l)
    def __repr__(self):
        return repr(self._l)
    def __len__(self):
        return len(self._l)
    def __contains__(self,value):
        return value in self._l
    def __bool__(self):
        return bool(self._l)
    def add(self,value):
        self._l.append(value)
    #индексирование элементов
    # def __setitem__(self,index,value):
    #     self._l[index]=value
    def __getitem__(self,index):
        if isinstance(index,tuple):
            return [self._l[i] for i in index]
        elif index==Ellipsis:
            #для инкапсуляции собственной коллекции
            return self._l.copy()
        return self._l[index]
    def __iter__(self):
        return MyListIterator(self._l)

class MyListIterator:
    def __init__(self,lst,i=0):
        self._lst=lst
        self._i=i
    def __iter__(self):
        return (MyListIterator(self._lst, self._i))

    def __next__(self):
        if self._i>=len(self._lst):
            raise StopIteration
        self._i+=1
        return self._lst[self._i-1]
