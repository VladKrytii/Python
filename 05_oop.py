# Task 1 

from abc import ABC, abstractmethod

class Ship(ABC):
    def __init__(self, name, displacement):
        self.name = name
        self.displacement = displacement

    @abstractmethod
    def ship_info(self):
        pass

class Frigate(Ship):
    def __init__(self, name, displacement, weapon_system):
        super().__init__(name, displacement)
        self.weapon_system = weapon_system

    def ship_info(self):
        return (f"Фрегат '{self.name}':: водотоннажність {self.displacement} тонн, "
                f"озброєння :: {self.weapon_system}")

class Destroyer(Ship):
    def __init__(self, name, displacement, speed):
        super().__init__(name, displacement)
        self.speed = speed

    def ship_info(self):
        return (f"Есмінець '{self.name}':: водотоннажність {self.displacement} тонн, "
                f"максимальна швидкість :: {self.speed} вузлів")

class Cruiser(Ship):
    def __init__(self, name, displacement, crew_size):
        super().__init__(name, displacement)
        self.crew_size = crew_size

    def ship_info(self):
        return (f"Крейсер '{self.name}':: водотоннажність {self.displacement} тонн, "
                f"екіпаж :: {self.crew_size} осіб")

if __name__ == "__main__":
    frigate = Frigate("Name", 4500, "Rokets")
    destroyer = Destroyer("Арлі Берк", 9500, 40)
    cruiser = Cruiser("Test", 13000, 550)

    print(frigate.ship_info())
    print(destroyer.ship_info())
    print(cruiser.ship_info())



# Task 2

class Airplane:
    def __init__(self, model, passenger_count, max_passengers):
        self.model = model
        self._passenger_count = 0
        self.max_passengers = max_passengers
        self.passenger_count = passenger_count

    @property
    def passenger_count(self):
        return self._passenger_count

    @passenger_count.setter
    def passenger_count(self, count):
        if 0 <= count <= self.max_passengers:
            self._passenger_count = count
        else:
            raise ValueError(
                f"Кількість пасажирів повинна бути у межах від 0 до {self.max_passengers}"
            )

    def __eq__(self, other):
        if isinstance(other, Airplane):
            return self.model == other.model
        return False

    def __add__(self, count):
        self.passenger_count += count
        return self

    def __sub__(self, count):
        self.passenger_count -= count
        return self

    def __iadd__(self, count):
        return self.__add__(count)

    def __isub__(self, count):
        return self.__sub__(count)

    def __lt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers < other.max_passengers
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers <= other.max_passengers
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers > other.max_passengers
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Airplane):
            return self.max_passengers >= other.max_passengers
        return NotImplemented

    def __int__(self):
        return self.passenger_count

    def __str__(self):
        return self.model


if __name__ == "__main__":
    airplane1 = Airplane("Boeing 777", 130, 200)
    airplane2 = Airplane("Airbus A32", 155, 180)

    print(airplane1 == airplane2)

    airplane1 += 40
    print(f"{airplane1.model}: {int(airplane1)} пасажирів")

    airplane1 -= 20
    print(f"{airplane1.model}: {int(airplane1)} пасажирів")

    print(airplane1 > airplane2)
    print(airplane1 < airplane2)

    print(str(airplane1))

    try:
        airplane1 += 50 
    except ValueError as e:
        print(e)

    try:
        airplane1 -= 199
    except ValueError as e:
        print(e)