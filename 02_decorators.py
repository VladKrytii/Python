# Task 1

import time

def calculate_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Час виконання ---> {end_time - start_time:.2f}")
        return result
    return wrapper

@calculate_time
def generate_even_numbers():
    return [x for x in range(0, 100001, 2)]

even_numbers = generate_even_numbers()
print("Парні числа ::", even_numbers[:100000])



# Task 2

def modify_negative_params(func):
    def wrapper(*args, **kwargs):
        modified_args = tuple(1 if isinstance(arg, (int, float)) and arg < 0 else arg for arg in args)
        modified_kwargs = {
            key: 1 if isinstance(value, (int, float)) and value < 0 else value 
            for key, value in kwargs.items()
        }
        return func(*modified_args, **modified_kwargs)
    return wrapper

@modify_negative_params
def sample_function(*args, **kwargs):
    print("Аргументи :: ", args)
    print("Іменовані аргументи :: ", kwargs)

sample_function(10, -3, "red", -1, 200, extra=-5, color="blue")