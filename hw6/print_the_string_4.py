str_ = input('Введіть рядок у якому більше 15 символів:\n')
print('Символ №3 = \'{}\''.format(str_[2]))
print('Передостанній символ = \'{}\''.format(str_[-2]))
print('Перші 5 символів: \'{}\''.format(str_[0:5]))
print('Всі, крім 2 крайніх: \'{}\''.format(str_[0:-2]))
if len(str_) % 2 == 0:
    print('Символи з парними індексами: \'{}\''.format(str_[0:-1:2]))
    print('Символи з непарними індексами: \'{}{}\''.format(str_[1:-1:2], str_[-1]))
else:
    print('Символи з парними індексами: \'{}{}\''.format(str_[0:-1:2], str_[-1]))
    print('Символи з непарними індексами: \'{}\''.format(str_[1:-1:2]))
print('Символи у зворотньому порядку: \'{}\''.format(str_[::-1]))
print('Довжина рядка = \'{}\''.format(len(str_)))
