
def input_int(string_int: str):
    """Функція перевіряє чи введене значення є ціле число"""
    while True:
        if string_int.isdigit() is not True:
            string_int = input('Ведіть дані ще раз: ')
        else:
            str_to_int = int(string_int)
            break
    return str_to_int


def search_number(low_limit, up_limit):
    """Функція перевіряє чи числа прості у заданому діапазоні!"""
    while low_limit <= up_limit:
        if (low_limit % 2 == 0 and low_limit // 2 == 1) or \
                (low_limit % 3 == 0 and low_limit // 3 == 1) or \
                (low_limit % 5 == 0 and low_limit // 5 == 1) or \
                (low_limit % 7 == 0 and low_limit // 7 == 1):
            yield low_limit
        elif low_limit % 2 == 0 or low_limit % 3 == 0 or low_limit % 5 == 0 or \
                low_limit % 7 == 0:
            low_limit += 1
            continue
        else:
            yield low_limit
        low_limit += 1


if __name__ == "__main__":
    low_lim, up_lim = input("Введіть нижню межу пошуку простого числа: "), \
                      input("Введіть верхню межу пошуку простого числа: ")
    a = input_int(low_lim)
    b = input_int(up_lim)
    if a < b:
        lst = []
        for ele in search_number(a, b):
            lst.append(ele)
        print(f'Прості числа в діапазоні {a} - {b}: ', lst)
    else:
        lst = []
        for ele in search_number(b, a):
            lst.append(ele)
        print(f'Прості числа в діапазоні {b} - {a}: ', lst)
