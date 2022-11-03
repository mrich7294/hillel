import sys

numer = input('Введіть число від 3 до 9: ')
if numer.isdigit() is False or int(numer) < 3 or int(numer) > 9:
    print('Введено некоректні дані!')
    sys.exit()
else:
    num = int(numer)
    numer = ''
    for i in range(1, num + 1):
        numer += str(i)
        print(numer, numer[-2::-1], sep='')

    print()
    numer = ''
    for j in range(1, num + 1):
        numer += str(j)
        var = numer + numer[-2::-1]
        print(var.rjust(20))

    print()
    numer = ''
    for k in range(1, num + 1):
        numer += str(k)
        var_1 = numer + numer[-2::-1]
        print(var_1.center(20))

