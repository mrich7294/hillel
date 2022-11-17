import random
n = input('Введіть розмір словника: ')
while n.isdigit() is not True:
    print('Необхідно ввести ціле число!')
    n = input('Введіть розмір словника: ')
n = int(n)
lst_1 = [(random.randint(10, 250)) for i in range(n)]
lst_2 = [(random.randint(-50, 0)) for j in range(n)]
my_dict = dict(zip(lst_1, lst_2))
print(my_dict)
