str_1 = 'python is good language to code'
value = 0
lst_1 = []
my_dict = {lk: value for lk in str_1}
my_dict.pop(' ')  # якщо потрібно прибрати ключ = пробіл
for j in my_dict.keys():
    count = 0
    if str_1.find(j) != -1:
        for i in str_1:
            if i == j:
                count += 1
        lst_1.append(count)
key = my_dict.keys()
my_dict = dict(zip(key, lst_1))
print('Це словник із букв рядка str_1, де ключ - це буква рядка, а значення - '
      'скільки раз ця буква повторяється!')
print(my_dict)
