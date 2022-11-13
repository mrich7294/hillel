import random
# lst_oven, lst_not_oven = [], []
lst = [(random.randint(0, 100)) for i in range(15)]
print('Вхідні дані:', lst)
# for j in range(len(lst)):
#     if lst[j] % 2 == 0:
#         lst_oven.append(lst[j])
#     elif lst[j] % 2 > 0:
#         lst_not_oven.append(lst[j])
lst_oven = [lst[j] for j in range(len(lst)) if lst[j] % 2 == 0]
lst_not_oven = [lst[j] for j in range(len(lst)) if lst[j] % 2 > 0]
print(f'Список парних чисел: {lst_oven}. Сума = {sum(lst_oven)}\n'
      f'Список непарних чисел: {lst_not_oven}. Сума = {sum(lst_not_oven)}')
if sum(lst_not_oven) > sum(lst_oven):
    print('Так, сума непарних чисел у списку більша за суму парних чисел!')
else:
    print('Ні, сума парних чисел у списку більша за суму непарних чисел або '
          'сума рівна!')
