class Auto:
    class __Motor:
        def __init__(self,song):
            self.__song=song
        def song(self):
            return self.__song
        def set_song(self, song):
            self.__song=song
    # a=Motor()
    def __init__(self,song):
        self.__motor=Auto.__Motor(song)
        # self.__motor = Auto.a
        # self.__motor.set_song(song)
    def go(self):
        return self.__motor.song()
    def repair(self,new_song):
        self.__motor.set_song(new_song)


a=Auto("brrrrr")
print(a.go())
b=Auto("rrrr")
print(b.go())
print(a.go())
a.repair("BRRR")
print(a.go())
