import random
# list_ = []
# new_list = []
list_1 = [(random.randint(10, 250)) for i in range(20)]
print('Вхідні дані: \n', list_1)
# for j in range(len(list_1)):
#     if list_1[j] % 20 != 0:
#         new_list.append(list_1[j])
list_1 = [list_1[j] for j in range(len(list_1)) if list_1[j] % 20 != 0]
print('Результат: \n', list_1)
