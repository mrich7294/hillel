import random

my_dict = {i: random.randint(1, 5) for i in range(1, 21)}
print('Це словник довжиною 20 елементів:\n', my_dict)
dob = 1
for (k, v) in my_dict.items():
    dob *= v
print('Це добуток значень словника довжиною 20 елементів:\n', dob)
