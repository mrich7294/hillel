lst = []
sum_, ser = 0, 0
min, max = 1000000, 0
even, not_even = 0, 0
while True:
    numb = int(input('Введіть число: '))
    if numb == 0:
        print('Це кінець!')
        print('Наш масив виглядає так:\n', lst)
        break
    else:
        lst.append(numb)
        # print(lst)
for i in range(0, len(lst)):
    sum_ += lst[i]
    if lst[i] >= max:
        max = lst[i]

for i in range(0, len(lst)):
    if lst[i] <= min:
        min = lst[i]

for i in range(0, len(lst)):
    if lst[i] % 2 == 0:
        even += 1
    else:
        not_even += 1

ser = sum_/len(lst)
print(f'Сума = {sum_} \nСереднє арифметичне = %.2f' % ser)
print(f'Максимальне значення = {max} \nМінімальне значення = {min}')
print(f'Парних чисел = {even} \nНе парних чисел = {not_even}')
