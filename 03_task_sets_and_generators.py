# Task 1
cities = {"Kyiv",
         "Lviv", 
         "Rivne", 
         "Dnipro", 
         "Kharkiv", 
         "Zaporizhzhia", 
         "Vinnytsia", 
         "Ivano-Frankivsk", 
         "Odesa", 
         "Poltava"
         }

print("1.Множина міст ---> ", cities)

# Task 2
cities_1 = {"Kyiv", "Lviv", "Odessa", "Dnipro", "Kharkiv"}
cities_2 = {"Lviv", "Odessa", "Poltava", "Chernihiv", "Zaporizhzhia"}

common_cities = cities_1 & cities_2
print("2. Міста, які є в обох множинах ---> ", common_cities)

# Task 3
only_in_first = cities_1 - cities_2
print("3. Міста тільки з першої множини ---> ", only_in_first)

# Task 4
only_in_second = cities_2 - cities_1
print("4. Міста тільки з другої множини ---> ", only_in_second)

#Task 5
unique_cities = cities_1 ^ cities_2
print("5. Унікальні міста в обох множинах ---> ", unique_cities)


# Generators
# Task 1

def odd_numbers_generator(start, end):
    return (num for num in range(start, end + 1) if num % 2 != 0)

start = 3
end = 22
odd_numbers = odd_numbers_generator(start, end)
print("Непарні числа в діапазоні :: ", list(odd_numbers))


# Task 2

def outside_range_generator(numbers, range_start, range_end):
    return (num for num in numbers if num < range_start or num > range_end)

numbers = [1, 7, 11, 15, 27]
range_start = 5
range_end = 12
outside_values = outside_range_generator(numbers, range_start, range_end)
print("Числа поза діапазоном ---> ", list(outside_values))