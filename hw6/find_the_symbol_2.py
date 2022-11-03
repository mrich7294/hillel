str_ = input('Введіть рядок:\n')
char_ = input('Введіть символ для пошуку:\n')
count = 0
if str_.find(char_) == -1:
    print('Цього символу в рядку немає.')
else:
    for i in str_:
        if i == char_:
            count = count + 1
print(f'Символів \'{char_}\' у рядку =', count)
