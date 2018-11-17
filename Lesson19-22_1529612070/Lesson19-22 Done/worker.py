class Worker:

    def __init__(self, name="No name", service=0, wagers=0, hours=0, salary=0):
        self.name = name
        self.service = service
        self.wagers = wagers
        self.hours = hours
        if salary:
            self.salary = salary
        else:
            self.set_salary()

    def info(self):
        return "last name              : {}\n"  \
                "length of service      : {} years\n" \
                "hourly wagers          : ${}\n" \
                "number of hours worked : {} hours\n" \
                "salary                 : ${}".format(self.name, self.service, self.wagers,
                                                      self.hours, self.salary)

    def get_info(self):
        return print(self.info())

    def save_info(self):
        with open("{}.txt".format(self.name), "w", encoding="UTF-8") as f:
            f.write(self.info())

    def set_salary(self):
        if self.service < 1:
            self.salary = self.wagers * self.hours
        elif 1 <= self.service < 3:
            self.salary = round(self.wagers * self.hours * 1.05)
        elif 3 <= self.service < 5:
            self.salary = round(self.wagers * self.hours * 1.08)
        elif 5 <= self.service:
            self.salary = round(self.wagers * self.hours * 1.15)

    def set_all(self):
        self.set_name()
        self.set_service()
        self.set_wagers()
        self.set_hours()

    def set_name(self):
        self.name = input("Input last name, please: ")

    def set_service(self):
        self.service = ""
        while not self.service.isdigit():
            self.service = input("Input length of service, please: ")
        self.service = int(self.service)
        self.set_salary()

    def set_wagers(self):
        self.wagers = ""
        while not self.wagers.isdigit():
            self.wagers = input("Input hourly wagers, please: ")
        self.wagers = int(self.wagers)
        self.set_salary()

    def set_hours(self):
        self.hours = ""
        while not self.hours.isdigit():
            self.hours = input("Input number of hours worked, please: ")
        self.hours = int(self.hours)
        self.set_salary()


if __name__ == '__main__':
    alex = Worker("Alex", salary=200)
    alex.get_info()
    daniel = Worker("Daniel", 3, 200, 1)
    daniel.get_info()
