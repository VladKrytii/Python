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
