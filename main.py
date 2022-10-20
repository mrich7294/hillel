iter_ = 1000
print('Введіть ітерацію')
i = input()
i = int(i)
while i < iter_:
    iter_ += 1
    print('Введіть значення')
    b = input()
    if b == "1":
        print('This true {}'.format(i))
    elif b == "2":
        print('This false {}'.format(i))
    else:
        print("This false")
        break
