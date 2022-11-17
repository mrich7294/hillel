import random

n = input('Введіть розмір списків: N = ')
while n.isdigit() is not True:
    print('Необхідно ввести ціле число!')
    n = input('Введіть розмір списку: N = ')
n = int(n)
lst_1 = [random.randint(0, 30) for i in range(n)]
lst_2 = [random.randint(10, 40) for i in range(n)]
print(f'Це наш список № 1:\n{lst_1}\nЦе наш список № 2:\n{lst_2}')
print(f'В списку зустрічається {len(set(lst_1 + lst_2))} різних чисел:')
print(f'{set(lst_1 + lst_2)}')
