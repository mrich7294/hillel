import random
list_ = []
new_list = []
list_ = [(random.randint(10, 250)) for i in range(20)]
print('Вхідні дані: \n', list_)
for j in range(len(list_)):
    if list_[j] % 20 != 0:
        new_list.append(list_[j])
print('Результат: \n', new_list)