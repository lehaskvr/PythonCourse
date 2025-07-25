class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

    def fare(self):
        fare = self.capacity * 100
        return fare


class Bus(Vehicle):
    def __init__(self, name, mileage, capacity):
        super().__init__(name, mileage, capacity)

    def technical_service(self):
        return self.capacity * 10

    def ecological_dues(self):
        return self.capacity * 5

    def total_fare(self):
        return self.capacity * 100 + self.capacity * 10 + self.capacity * 5


school_bus = Bus("Школьный Volvo", 12, 50)
print(f"🚌 Вместимость: {school_bus.capacity} пассажиров.")
print(f"🚌 Общая стоимость проезда: {school_bus.capacity} * 100 = {school_bus.fare()} руб.")
print(f"🚌 Техобслуживание(10%): {school_bus.technical_service()}")
print(f"🚌 Экосбор (5%): {school_bus.ecological_dues()}")
print(f"🚌 Итоговая стоимость: {school_bus.total_fare()}")
