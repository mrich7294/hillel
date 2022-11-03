word_1, word_2 = input('Введіть два слова через пробіл: ').split()
while True:
    if word_1.isalpha() is not True or word_2.isalpha() is not True:
        print('Зверніть увагу!!! Необхідно ввести два слова без розділових знаків та цифр через пробіл.')
        word_1, word_2 = input('Введіть два слова через пробіл: ').split()
    elif word_1.isalpha() is True and word_2.isalpha() is True:
        print(word_1[::-1].capitalize(), word_2[::-1].capitalize())
        break
