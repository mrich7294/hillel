import random


def search_number(low_limit, up_limit):
    """Перевіряє чи числа прості!"""
    lst = []
    for i in range(low_limit, up_limit + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return print(f'Прості числа в діапазоні {low_limit} - {up_limit}: ', lst)


low_num, up_num = random.randint(2, 150), random.randint(20, 100)
# print(low_num, up_num)
if low_num > up_num:
    low_num, up_num = up_num, low_num
# print(low_num, up_num)
search_number(low_num, up_num)
