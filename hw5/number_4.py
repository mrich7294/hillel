numb = int(input('Введіть число: '))
lst = []
for i in range(0, 1000):
    while numb >= (i ** 2):
        lst.append(i ** 2)
        break
print(lst)
