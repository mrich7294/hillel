lst = ['Password', 'P@$$wd', 'Parol', '']
i = 0
attempt = int(input("Enter the number of password attempts: "))
passwd = input("Enter the password: ")
for i in range(attempt):
    if passwd not in lst:
        print("Your password is not correct! Try again!")
        passwd = input("Enter the password: ")
    else:
        print("Your password is correct!!!")
        break
