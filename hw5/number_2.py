numb = int(input('Введіть число: '))
lst = []
k = 0
numb2 = 0
x = numb
while numb > 0:
    lst.append(numb % 10)
    numb = numb // 10
    k = len(lst)
while numb2 < x:
    for i in range(1, k + 1):
        if (i == 1) and ((numb2 ** 2) % 10 == numb2):
            if numb2 == 0:
                continue
            else:
                print(f'{numb2} * {numb2} =', numb2 ** 2)
        elif (i == 2) and ((numb2 ** 2) % 100 == numb2) and numb2 > 9:
            print(f'{numb2} * {numb2} =', numb2 ** 2)
        elif (i == 3) and ((numb2 ** 2) % 1000 == numb2) and numb2 > 99:
            print(f'{numb2} * {numb2} =', numb2 ** 2)
        elif (i == 4) and ((numb2 ** 2) % 10000 == numb2) and numb2 > 999:
            print(f'{numb2} * {numb2} =', numb2 ** 2)
        elif (i == 5) and ((numb2 ** 2) % 100000 == numb2) and numb2 > 9999:
            print(f'{numb2} * {numb2} =', numb2 ** 2)
        elif (i == 6) and ((numb2 ** 2) % 1000000 == numb2) and numb2 > 99999:
            print(f'{numb2} * {numb2} =', numb2 ** 2)

    numb2 += 1
