import time

print('Загадайте число від 1 до 99')
time.sleep(2)
var1, var2 = 0, 100
var3 = 50
count = 0
while True:
    print('Це число: ', var3)
    c = input('Введіть значення: >, < або = \n')
    if c == '=':
        print('Ви загадали число - ', var3)
        break
    elif c == '>':
        var1 = var3
        var3 = (var1 + var2) // 2
    elif c == '<':
        var2 = var3
        var3 = (var1 + var2) // 2
    else:
        print('The end')
        break