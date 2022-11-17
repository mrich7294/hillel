import random

n = input('Введіть розмір списку: N = ')
while n.isdigit() is not True:
    print('Необхідно ввести ціле число!')
    n = input('Введіть розмір списку: N = ')
n = int(n)
lst = [random.randint(0, 20) for i in range(n)]
print(f'Це наш список:\n', lst)
print(f'В списку зустрічається {len(set(lst))} різних чисел.')