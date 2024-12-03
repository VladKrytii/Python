# 1
fruits = ("apple", "orange", "banana")

fruit_name = input("Введіть назву фрукта :: ")

count = fruits.count(fruit_name)
print(f"Фрукт '{fruit_name}' зустрічається {count} разів")


# 2

fruits = ("banana", "apple", "bananamango", "mango", "strawberry-banana")

fruit_name = input("Введіть назву фрукта:: ")

count = sum(1 for fruit in fruits if fruit_name in fruit)
print(f"Назва '{fruit_name}' зустрічається в {count} елементах")


# 3

car_brand = ("Audi", "Toyota" ,"BMW", "Mercedes")

old_name = input("Введіть назву виробника для заміни :: ")
new_name = input("Введіть нове слово для заміни :: ")

updated_cars = tuple(new_name if car == old_name else car for car in car_brand)

print("Update --->", updated_cars)

# 4

numbers = (1, 3, 6, 12, 17, 33, 55, 72, 122)

digit_count = {}

for number in numbers:
    digits = len(str(abs(number)))
    digit_count[digits] = digit_count.get(digits, 0) + 1

for digits, count in sorted(digit_count.items()):
    print(f"{digits} цифра --> {count} елемент")