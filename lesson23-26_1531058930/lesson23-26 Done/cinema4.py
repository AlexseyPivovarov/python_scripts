sessions = [
    {"name": "Потема", "start_time": 0, "end_time": 80, "hall": "Красный", "seats": [True for _ in range(10)]},
    {"name": "Потема", "start_time": 120, "end_time": 200, "hall": "Синий", "seats": [True for _ in range(10)]}
    ]


class Cinema:

    def __init__(self, name: str, halls: dict):
        self.name = name
        self.halls = halls

    def set_sale_seat(self, session: dict, place_number: int):
        session["seats"][place_number - 1] = False

    def get_data(self, key: str, to_find):
        return [item for item in sessions if item[key] == to_find]

    def set_session(self, film: str, hall: str, start_time: int, end_time: int):
        for session in self.get_data("hall", hall):
            if (session["start_time"] <= start_time <= session["end_time"]) or \
               (start_time <= session["start_time"] <= end_time):
                raise Exception("Time are busy")
        else:
            sessions.append({"name": film, "start_time": start_time, "end_time": end_time, "hall": hall,
                             "seats": [True for _ in range(self.halls[hall])]})


myCinema = Cinema("Аризона", {"Красный": 10, "Синий": 10})


print(myCinema.get_data("name", "Потема"))
print(myCinema.get_data("start_time", 120))
print(myCinema.get_data("hall", "Красный"))


