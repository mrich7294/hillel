
def decor(func):

    def two_values():
        firth_value, second_value = func()
        try:
            result = float(firth_value) + float(second_value)
        except (TypeError, ValueError) as err:
            print(f'Вийняток класу {err.__class__.__name__}!\n'
                  'Одне із значень не є числом, виконується конкатенація.')
            result = str(firth_value) + str(second_value)
            print(f'Результат конкатенації: {firth_value} + {second_value} '
                  f'= {result}')
        else:
            print('Вийнятків не було!')
            print(f'Результат довадання: {firth_value} + {second_value} '
                  f'= {result}')
        finally:
            print("Це 'finally' виконується в будь якому випадку... ")
    return two_values


@decor
def input_two_values():
    """
    Перевіряє чи введено два значення.\n
    :return: word_1, word_2 -> string
    """
    str_tohandle = input('Введіть два значення через пробіл: ')
    while len(str_tohandle.split()) != 2:
        str_tohandle = input('Введіть два значення через пробіл: ')
    word_1, word_2 = str_tohandle.split()
    return word_1, word_2


if __name__ == "__main__":
    input_two_values()
