# Task 1

def odd_numbers_in_range(start, end):
    return (num for num in range(start, end + 1) if num % 2 != 0)

start = 1
end = 22
odd_numbers = odd_numbers_in_range(start, end)

print(f"Непарні числа в діапазоні від {start} до {end}")
print(list(odd_numbers))


# Task 2

def values_outside_range(lst, start, end):
    return (value for value in lst if value < start or value > end)

lst = [1, 3, 7, 11, 23, 27]
start = 5
end = 15
filtered_values = values_outside_range(lst, start, end)

print(f"Значення зі списку {lst}, що не входять у діапазон від {start} до {end}")
print(list(filtered_values))