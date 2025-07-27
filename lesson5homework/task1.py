class Vehicle:
    def __init__(self, name, mileage, capacity):
        if isinstance(name, str):
            self._name = name
        else:
            raise ValueError("Некорректное имя автобуса")
        if mileage > 0:
            self._mileage = mileage
        else:
            raise ValueError("Некорректный расход топлива у автобуса")
        if capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Некорректная вместимость автобуса")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str):
            self._name = new_name
        else:
            raise ValueError("Некорректное имя автобуса")

    @property
    def mileage(self):
        return self._mileage

    @mileage.setter
    def mileage(self, new_mileage):
        if new_mileage > 0:
            self._mileage = new_mileage
        else:
            raise ValueError("Некорректный расход топлива у автобуса")

    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, new_capacity):
        if new_capacity > 0:
            self._capacity = new_capacity
        else:
            raise ValueError("Некорректная вместимость автобуса")

    def fare(self):
        fare = self.capacity * 100
        return fare


class Bus(Vehicle):
    def technical_service(self):
        return self.capacity * 15

    def ecological_dues(self):
        return self.capacity * 5

    def total_fare(self):
        return self.fare() + self.technical_service() + self.ecological_dues()

    def get_info(self):
        print("Название автобуса:", self._name)
        print("Расход топлива:", self._mileage, "литров на 100 километров")
        print("Вместимость:", self._capacity, "пассажиров")
        print("Общая стоимость проезда:", self.fare(), "руб")
        print("Техобслуживание:", self.technical_service(), "руб")
        print("Экосбор:", self.ecological_dues(), "руб")
        print("Общая стоимсоть:", self.total_fare(), "руб")


school_bus = Bus("Школьный Volvo", 12, 50)

school_bus.get_info()
