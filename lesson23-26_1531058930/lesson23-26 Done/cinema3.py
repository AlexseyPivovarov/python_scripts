class Film:

    def __init__(self, name, time):
        self.name = name
        self.time = time

    def get_info(self):
        return "{}: {}м".format(self.name, self.time)


# ---------------------------------------------------------------------------------------------------------------------
class Seat:

    def __init__(self):
        self.reserved = True

    def set_reserved(self):
        self.reserved = False

    def set_unreserved(self):
        self.reserved = True

    def get_info(self):
        return str(self.reserved)


# ---------------------------------------------------------------------------------------------------------------------
class Seans:

    def __init__(self, film: Film, start_time: int, number_of_seats: int):
        self.film = film
        self.start = start_time
        self.end = start_time + film.time
        self.seats = tuple([Seat() for _ in range(number_of_seats)])

    def get_seats_info(self):
        return "\n".join(["{:0>2} - {}".format(i, j.get_info()) for i, j in enumerate(self.seats)])


# ---------------------------------------------------------------------------------------------------------------------
class Hall:

    def __init__(self, name: str, number_of_seats: int):
        self.name = name
        self.number_of_seats = number_of_seats
        self.time_scale = []

    def set_film_to_seans(self, film: Film, start_time: int):
        temp = Seans(film, start_time, self.number_of_seats)
        for item in self.time_scale:
            if (item.start <= temp.start <= item.end) or (temp.start <= item.start <= temp.end):
                raise Exception("Busy time")
        else:
            self.time_scale.append(temp)
            self.time_scale.sort(key=lambda i: i.start)

    def get_info(self):
        return ";  ".join(["{}: {}ч {:0>2}м - {}ч {:0>2}м"
                          "".format(item.film.name, (item.start // 60) % 24, item.start % 60,
                                    (item.end // 60) % 24, item.end % 60) for item in self.time_scale])


# ---------------------------------------------------------------------------------------------------------------------
class Cinema:

    def __init__(self, name: str, halls_names: tuple, number_of_seats_in_the_halls: tuple):
        self.name = name
        self.halls = tuple([Hall(i, j) for i, j in zip(halls_names, number_of_seats_in_the_halls)])
        self.poster = []


# ---------------------------------------------------------------------------------------------------------------------
class CinemaApi(Cinema):

    def __init__(self, name: str, halls_names: tuple, number_of_seats_in_the_halls: tuple):
        super().__init__(name, halls_names, number_of_seats_in_the_halls)

    def set_film(self, name: str, time: int):
        self.poster.append(Film(name, time))
        self.poster.sort(key=lambda item: item.name)

    def get_poster_info(self):
        return "; ".join([item.get_info() for item in self.poster])


# ---------------------------------------------------------------------------------------------------------------------
if __name__ == '__main__':
    myCinema = CinemaApi("My Cinema", ("Red", "Blue"), (10, 10))

    myCinema.set_film("Чобиты", 80)
    myCinema.set_film("Дневник будущего", 220)
    myCinema.set_film("Торадора", 40)
    print(myCinema.get_poster_info())

    # myCinema.set_film_to_seans(0, 1, 12)
    # myCinema.set_film_to_seans(0, 0, 21)
    # myCinema.set_film_to_seans(0, 2, 18)
    # print(myCinema.get_time_scale_info(0))
    #
    # myCinema.set_film_to_seans(1, 0, 12)
    # myCinema.set_film_to_seans(1, 2, 21)
    # myCinema.set_film_to_seans(1, 1, 18)
    # print(myCinema.get_time_scale_info(1))
    #
    # myCinema.set_ticket(0, 1, 2)
    # print(myCinema.get_seans_seats_info(0, 1))



