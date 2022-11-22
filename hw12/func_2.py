import random

numbers = [random.randint(1, 5) for _ in range(20)]
numbers_1 = [random.randint(1, 5) for __ in range(20)]

lambda_func = lambda x, y = 2: x ** y
mapped_numbers = list(map(lambda_func, numbers))
print('Передається один список для обробки у map: ', mapped_numbers)
lambda_func_1 = lambda x, y = 2: x ** y
mapped_numbers_1 = list(map(lambda_func, numbers, numbers_1))
print('Передається два списки для обробки у map: ', mapped_numbers_1)
