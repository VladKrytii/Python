# Task 1

class Passport:
    def __init__(self, first_name, last_name, country, passport_number):
        self.first_name = first_name
        self.last_name = last_name
        self.country = country
        self.passport_number = passport_number

    def __str__(self):
        return (f"Passport of {self.first_name} {self.last_name} "
                f"from {self.country}, Passport Number :: {self.passport_number}")

    def update_info(self, first_name=None, last_name=None, country=None, passport_number=None):
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if country:
            self.country = country
        if passport_number:
            self.passport_number = passport_number


class ForeignPassport(Passport):
    def __init__(self, first_name, last_name, country, passport_number, foreign_number, visas=None):
        super().__init__(first_name, last_name, country, passport_number)
        self.foreign_number = foreign_number
        self.visas = visas if visas else []

    def __str__(self):
        base_info = super().__str__()
        visas_info = ", ".join(self.visas) if self.visas else "No visas"
        return (f"{base_info}\nForeign Passport Number :: {self.foreign_number}, "
                f"Visas :: {visas_info}")

    def add_visa(self, visa):
        self.visas.append(visa)

    def remove_visa(self, visa):
        if visa in self.visas:
            self.visas.remove(visa)
        else:
            print(f"Visa '{visa}' not found in the list")

    def update_foreign_number(self, foreign_number):
        self.foreign_number = foreign_number



if __name__ == "__main__":
    passport = Passport("Igor", "Melnuk", "Ukraine", "123456")
    print(passport)
    
    passport.update_info(last_name="Kotenko", passport_number="1234567")
    print(passport)
    
    foreign_passport = ForeignPassport("Igor", "Melnuk", "Ukraine", "12345", "FP1122")
    print(foreign_passport)
    
    foreign_passport.add_visa("USA")
    foreign_passport.add_visa("Mexico")
    print(foreign_passport)
    
    foreign_passport.remove_visa("Mexico")
    print(foreign_passport)
    
    foreign_passport.update_foreign_number("FP1111")
    print(foreign_passport)