import random


def my_func(list_1, int_1):
    """Перевіряє чи є у списку 2 числа сума яких еквівалентна числу
    переданому 2-им параметром"""
    cnt = 0
    for i in range(len(list_1)):
        for j in range(len(list_1)):
            if list_1[j] + list_1[i] == int_1:
                cnt += 1
    if cnt > 0:
        bool_1 = True
    else:
        bool_1 = False
    return print(bool_1)

print('Перевіряє чи є у списку 2 числа сума яких еквівалентна числу '
      'переданому 2-им параметром:')
lst = [random.randint(1, 20) for x in range(20)]
a = random.randint(25, 35)
print(f'Список {lst}, другий параметр {a}')
my_func(lst, a)

lst_1 = [random.randint(15, 40) for _ in range(15)]
a_1 = random.randint(30, 55)
print(f'Список {lst_1}, другий параметр {a_1}')
my_func(lst_1, a_1)
