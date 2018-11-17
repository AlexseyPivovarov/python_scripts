from uuid import uuid4


def uid():
    return str(uuid4())


# ---------------------------------------------------------------------------------------------------------------------
class CommMeta(type):

    name = str

    def __new__(mcs, *args, **kwargs):
        mcs.name = args[0].lower()
        return super().__new__(mcs, *args, **kwargs)

    def __call__(cls, *args, **kwargs):
        if hasattr(args[0], cls.name):
            return getattr(args[0], cls.name)
        else:
            new = super().__call__(*args, **kwargs)
            setattr(args[0], cls.name, new)
            return new


# ---------------------------------------------------------------------------------------------------------------------
class Cinema:

    def __init__(self):
        self.all = dict


# ---------------------------------------------------------------------------------------------------------------------
class Film(metaclass=CommMeta):

    def __init__(self, cinema: Cinema):
        self.cin = cinema
        self.films = dict


# ---------------------------------------------------------------------------------------------------------------------
class Session(metaclass=CommMeta):

    def __init__(self, cinema: Cinema):
        self.cin = cinema
        self.sessions = dict


# ---------------------------------------------------------------------------------------------------------------------
class Hall(metaclass=CommMeta):

    def __init__(self, cinema: Cinema):
        self.cin = cinema
        self.halls = dict


# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    cinemas = Cinema()
    film = Film(cinemas)
    film.films = 123
    print(film.films)
    film2 = Film(cinemas)
    print(film2.films)
    session = Session(cinemas)
    hall = Hall(cinemas)



