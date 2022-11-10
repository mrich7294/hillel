# lst = []
new_list = []
lst = input('Введіть речення: ').split(" ")
while True:
    if len(lst) < 3:
        print('Зверніть увагу!!! Необхідно ввести більше двох слів.')
        lst = input('Введіть речення: ').split(" ")

    else:
        print('Це наш список:\n', lst)
        for j in range(len(lst)):
            if lst[j] != '':
                new_list.append(lst[j])

    new_list.sort()  # сортувати з урахуванням регістру!
    print('Відсортований та відфільтрований список: \n', new_list)
    for i in range(len(new_list)):
        print(f'{i:{2}} {new_list[i]}')
    print('Кількість слів =', len(new_list))
    break
