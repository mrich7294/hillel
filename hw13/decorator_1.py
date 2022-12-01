import random


def my_decor(func):

    def inner_wrapper(lengt: int):
        my_set = func(lengt)
        lst = ['кратне 3', 'не кратне 3', 'парне', 'не парне']
        for i in my_set:
            if i % 3 == 0:
                if i % 2 == 0:
                    print(f'{i:^5} {lst[0]:14} {lst[2]:10}')
                else:
                    print(f'{i:^5} {lst[0]:14} {lst[3]:10}')
            elif i % 2 == 0:
                print(f'{i:^5} {lst[1]:14} {lst[2]:10}')
            else:
                print(f'{i:^5} {lst[1]:14} {lst[3]:10}')
    return inner_wrapper


def input_int(string_int: str):
    """Функція перевіряє чи введене значення є ціле число"""
    while True:
        if string_int.isdigit() is not True:
            print('Введіть ціле число!')
            string_int = input('Ведіть дані ще раз: ')
        else:
            str_to_int = int(string_int)
            break
    return str_to_int


@my_decor
def create_set(length_1: int):
    """Функція створює множину заданої величини та заповнює її рандомними
    значеннями"""
    my_set = {random.randint(0, length_1+50) for _ in range(length_1)}
    while True:
        if len(my_set) < length_1:
            my_set.add(random.randint(0, length_1+50))
        else:
            print(f'Це множина величиною {len(my_set)} елементів:\n{my_set} ')
            break
    return sorted(my_set)


if __name__ == "__main__":
    numb = input('Введіть кількість елементів у множині: ')
    n = input_int(numb)
    create_set(n)
