import random

n = input('Введіть розмірність матриці: N = ')
while n.isdigit() is not True:
    print('Необхідно ввести ціле число!')
    n = input('Введіть розмірність матриці: N = ')
n = int(n)
matrix = [
    [random.randint(-50, 50) for i in range(j, j + n)]
    for j in range(0, n)
]
print('Вхідні дані:\n', matrix)
print('Вихідні дані:')
summ, var = 0, 0
sum_row = 0
for m in matrix:
    sum_row += m[n-1]
    for k in range(len(m)):
        elem = m[k]
        print(f'{elem:^6}', end='')
        if var == k:
            summ += m[k]
    print()
    var += 1
print('Сума чисел по діагоналі =', summ)
print('Сума чисел остнанього стовбця', sum_row)
