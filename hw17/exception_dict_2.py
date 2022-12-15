

def dict_handler(link_on_dict: dict, my_key, default_value):
    try:
        link_on_dict.setdefault(my_key, default_value)
    except KeyError:
        link_on_dict[my_key] = default_value
        print(link_on_dict[my_key])
    except TypeError:
        print("Ключ 'key' змінюваний тип данних, він не може бути ключем "
              "словника!")
    else:
        print('Виключень не було!')
    finally:
        print(f"Це 'finally' виконується в будь якому випадку... "
              f"Ключ пошуку: \'{my_key}\', тип даних {type(my_key)}.")
    return link_on_dict[my_key]


if __name__ == "__main__":
    my_dict = {100: 'start', 20: 'stop'}
    key = ['we']
    try:
        a = dict_handler(my_dict, key, 'default')
    except TypeError as er:
        print(f'Помилка класу {er.__class__.__name__}, недопустимий тип '
              f'даних ключа!')
    else:
        print(f'Значення по заданому ключу = \'{a}\'')
        print(f'Мій словник: {my_dict}')
