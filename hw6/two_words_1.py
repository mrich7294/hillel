lst = []
lst = input('Введіть два слова через пробіл: ').split()
while True:
    if len(lst) < 2 or len(lst) >= 3 or lst[0].isalpha() is not True or lst[1].isalpha() is not True:
        print('Зверніть увагу!!! Необхідно ввести два слова без розділових знаків та цифр через пробіл.')
        lst = input('Введіть два слова через пробіл: ').split()
    elif lst[0].isalpha() is True and lst[1].isalpha() is True:
        word_1, word_2 = lst[0], lst[1]
        print(word_1[::-1].capitalize(), word_2[::-1].capitalize())
        break
