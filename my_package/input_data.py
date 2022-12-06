import sys


def password_requirements(func):

    def wrapper():
        """Фунцкція перевіряє чи задовільняє пароль умовам!"""
        passwd = func()
        while True:
            if passwd is None:
                print("Пароль містить символи табуляції або пустий!")
                passwd = func()
            elif len(passwd) < 8:
                print('Ваш пароль повинен містити не менше 8 символів!')
                passwd = func()
            else:
                cnt_digit, cnt_alpha = 0, 0
                for i in passwd:
                    if i.isdigit() is True:
                        cnt_digit = 1
                    elif i.isalpha() is True:
                        cnt_alpha = 1
                while True:
                    if cnt_digit < 1:
                        print('У вашому паролі повинно бути не менше 1 цифри!')
                        passwd = func()
                        break
                    elif cnt_alpha < 1:
                        print('У вашому паролі повинно бути не менше 1 літери!')
                        passwd = func()
                        break
                    else:
                        is_print = passwd.isprintable()
                        if passwd.isalnum() is False and is_print is True:
                            print(f'Ваш пароль {passwd} прийнято!!!')
                            sys.exit()
                        else:
                            print(
                                'У вашому паролі повинно бути не менше 1 '
                                'спеціального символу!')
                            passwd = func()
                            break
    return wrapper


@password_requirements
def input_password():
    """Функція запитує пароль у користувача"""
    passwd_requirements = "Пароль повинен задовільняти всі умови: не менше " \
        "8 символів, в тому числі не менше 1 букви, 1 цифри, 1 спеціального "\
        "символу та не містити символів табуляції!"
    cnt = 0
    print(passwd_requirements)
    password = input("Введіть пароль: ")
    if len(password) == 0:
        cnt = 1
    elif len(password) > 0:
        for i in password:
            if i.isspace() is True:
                cnt = 1
    if cnt == 1:
        return None
    else:
        return password


def input_str_to_int(string_int: str) -> int:
    """Функція перевіряє чи введене значення є ціле число більше ніж 4"""
    while True:
        if string_int.isdigit() is not True:
            print('Введіть ціле число більше 4!')
            string_int = input('Ведіть дані ще раз: ')
        elif int(string_int) < 5:
            print('Понинно бути ціле число більше 4!')
            string_int = input('Ведіть дані ще раз: ')
        else:
            str_to_int = int(string_int)
            break
    return str_to_int


if __name__ == "__main__":
    pass