# Task 1
countries = {
    "Україна": "Київ",
    "Німеччина": "Берлін",
    "США": "Вашингтон"
}

while True:
    print("Меню ::")
    print("1. Додати країну та столицю")
    print("2. Видалити країну")
    print("3. Знайти столицю")
    print("4. Замінити столицю")
    print("5. Показати всі країни")
    print("6. Вийти")

    choice = input("Виберіть дію :: ")

    if choice == "1":
        country = input("Введіть країну :: ")
        capital = input("Введіть столицю :: ")
        countries[country] = capital
        print(f"Додано :: {country} ---> {capital}")

    elif choice == "2":
        country = input("Введіть країну для видалення :: ")
        if countries.pop(country, None):
            print(f"Країну '{country}' видалено")
        else:
            print(f"Країни '{country}' немає у списку")

    elif choice == "3":
        country = input("Введіть країну :: ")
        print(f"Столиця :: {countries.get(country, 'Країни немає у списку')}")

    elif choice == "4":
        country = input("Введіть країну :: ")
        if country in countries:
            capital = input("Введіть нову столицю :: ")
            countries[country] = capital
            print(f"Столицю для '{country}' змінено на '{capital}'")
        else:
            print(f"Країни '{country}' немає у списку")

    elif choice == "5":
        for country, capital in countries.items():
            print(f"{country} ---> {capital}")

    elif choice == "6":
        print("Exit.......")
        break

    else:
        print("Try again!!!")


# Task 2

import time

def timer(func):
    def wrapper():
        start = time.time()
        result = func()
        print(f"Час виконання ----> {time.time() - start:.5f} секунд")
        return result
    return wrapper

@timer
def get_even_numbers():
    return list(range(0, 100001, 2))

even_numbers = get_even_numbers()
print(f"Кількість парних чисел :: {len(even_numbers)}")