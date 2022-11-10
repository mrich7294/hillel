sum_credit = input('Введіть суму кредиту, яку ви хочете взяти: ')
time_year = input('Введіть кількість років, на скільки хочете взяти кредит: ')
while sum_credit.isdigit() is not True or time_year.isdigit() is not True:
    print('Необхідно ввести цілі числа!')
    sum_credit = input('Введіть суму кредиту, яку ви хочете взяти: ')
    time_year = input('Введіть кількість років, на скільки хочете взяти кредит: ')
percent, per = 0, 0
sum_percent = 0
sum_payment = 0
cnt, cont = 0, 0
time_year = int(time_year)
sum_credit = int(sum_credit)
time_month = time_year * 12
sum_payment = sum_credit / time_month
while cnt < time_year:

    print(f'Це рік кредитування № {cnt + 1}!\nСума заборгованості = {sum_credit:10.2f}.')
    print('Місяць оплати\t Нараховані % \tТіло кредиту \t\tСума до оплати')
    for i in range(1, 13):
        if cnt < 2:
            percent = 2
            sum_percent = sum_credit / time_month * percent / 100 * time_year
            # per = sum_credit / time_month * percent / 100
            # sum_percent = per / (1 - 1 / (1 + time_month * percent) ** time_month) * time_year
            sum_payment_all = sum_payment + sum_percent
            print(f' {i} {sum_percent:{2}2.2f} {sum_payment:{1}5.2f} {sum_payment_all:{2}1.2f}')
            sum_credit -= sum_payment

        elif cnt > 1:
            if cont == 0:
                print(f'Зверніть увагу!\nВаша відсоткова ставка зросла з 2 % до 4 %!')
                cont = 1
            percent = 4
            sum_percent = sum_credit / time_month * percent / 100 * time_year
            # per = sum_credit / time_month * percent / 100
            # sum_percent = per / (1 - 1 / (1 + time_month * percent) ** time_month) * time_year
            sum_payment_all = sum_payment + sum_percent
            print(f' {i:{2}2.2f} {sum_percent:{2}2.2f} {sum_payment:{1}5.2f} {sum_payment_all:{2}1.2f}')
            sum_credit -= sum_payment
    cnt += 1
