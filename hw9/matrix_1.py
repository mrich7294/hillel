import random

n = input('Введіть розмірність матриці: N = ')
# lst = []
while n.isdigit() is not True:
    print('Необхідно ввести ціле число!')
    n = input('Введіть розмірність матриці: N = ')
n = int(n)
matrix = [
    [random.randint(-n, -1) if j % 2 > 0 else j for i in range(j, j + n)]
    for j in range(0, n)
]
print(matrix)
for m in matrix:
    for k in range(len(m)):
        elem = m[k]
        print(f'{elem:^5}', end='')
    print()
