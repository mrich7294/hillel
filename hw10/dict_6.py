
poem = '''Любіть Україну, як сонце любіть,
як вітер, і трави, і води...
В годину щасливу і в радості мить,
любіть у годину негоди.
Любіть Україну у сні й наяву,
вишневу свою Україну,
красу її, вічно живу і нову,
і мову її солов'їну.
Без неї — ніщо ми, як порох і дим,
розвіяний в полі вітрами...
Любіть Україну всім серцем своїм
і всіми своїми ділами.
'''
res_text = ''
lst_2 = []
for j in poem:
    if j.isalnum():
        res_text += j
    else:
        res_text += ' '
lst_1 = list(res_text.split())
for i in range(len(lst_1)):
    cnt = 0
    for k in lst_1:
        # if k.lower() == lst_1[i].lower():
        if k == lst_1[i]:
            cnt += 1
    lst_2.append(cnt)

# 'Любіть' та 'любіть' це різні ключі,
# тому не приводив слова до спільного регістру

my_dict = dict(zip(lst_1, lst_2))
ls_max = [k for (k, v) in my_dict.items() if v == max(lst_2)]
ls_min = [k1 for (k1, v1) in my_dict.items() if v1 == min(lst_2)]
print('Це словник:\n', my_dict)
print(f'Слова, які зусрічається найменше разів: {min(lst_2)}\n', ls_min)
print(f'Слова, які зусрічається найбільше разів: {max(lst_2)}\n', ls_max)

