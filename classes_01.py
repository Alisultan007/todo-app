class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.__engine_on = False

    def __str__(self):
        return f'Car: {self.make} {self.model} {self.year}'

    def get_engine_status(self):  # get
        if self.__engine_on:
            return "Машина заведена"
        else:
            return "Машина заглушена"

    def set_engine_status(self, status):  # set
        if self.__engine_on == status:
            return f"Двигатель машины уже имеет статус {status}"
        else:
            self.__engine_on = status
            return f"Двигатель машины изменён на статус {status}"


if __name__ == '__main__':
    car1 = Car("Toyota", "RAV4", 1996)
    print(car1)
    # print(type(car1))

    car1.make = "Subaru"

    print(car1)
    print(car1.get_engine_status())
    print(car1.set_engine_status(True))
    print(car1.get_engine_status())