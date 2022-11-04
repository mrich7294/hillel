row = input('Введіть кількість стовпців для виведення: ')
while row.isdigit() is not True:
    print('Необхідно ввести ціле число!')
    row = input('Введіть кількість стовпців для виведення: ')
for i in range(int(row)+1):
    print(f'{i:{2}} {10 ** i:{20}}')
