low_lim, up_lim = input("Введіть нижню межу пошуку простого числа: "), \
                  input("Введіть верхню межу пошуку простого числа: ")


def input_int(string_int: str):
    """Функція перевіряє чи введене значення є ціле число"""
    while True:
        if string_int.isdigit() is not True:
            string_int = input('Ведіть дані ще раз: ')
        else:
            strin_int = int(string_int)
            break
    return strin_int


def search_number(low_limit, up_limit):
    """Функція перевіряє чи числа прості у заданому діапазоні!"""
    lst = []
    for i in range(low_limit, up_limit + 1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            lst.append(i)
    return print(f'Прості числа в діапазоні {low_limit} - {up_limit}: ', lst)


a = input_int(low_lim)
b = input_int(up_lim)
if a < b:
    search_number(a, b)
else:
    search_number(b, a)
