import sys

numer = input('Введіть число від 3 до 9: ')
if numer.isdigit() is False or int(numer) < 3 or int(numer) > 9:
    print('Введено некоректні дані!')
    sys.exit()
else:
    numer = int(numer)
    for i in range(1, numer + 2):
        for j in range(1, i - 1):
            print(j, end=" ")
        for j in range(i - 1, 0, -1):
            print(j, end=" ")
        print()
