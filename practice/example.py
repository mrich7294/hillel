# n = int(input())
# a = n % 10
# print(a)

# a = int(input("Input the number: "))
# n = 0
# while a > 0:
#     z = a % 10
#     a //= 10
#     n *= 10
#     n += z
# print(n)

# Колір клітинок рулетки
# a = int(input())
# if 0 < a <= 10:
#     if a % 2 > 0:  # непарне
#         print('красный')
#     else:
#         print('черный')
# elif 11 <= a <= 18:
#     if a % 2 > 0:
#         print('черный')
#     else:
#         print('красный')
# elif 19 <= a <= 28:
#     if a % 2 > 0:  # непарне
#         print('красный')
#     else:
#         print('черный')
# elif 29 <= a <= 36:
#     if a % 2 > 0:
#         print('черный')
#     else:
#         print('красный')
# elif a == 0:
#     print('зеленый')
# else:
#     print('ошибка ввода')

# Колір клітинок
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (a % 2 == 0 and b % 2 > 0) or (a % 2 > 0 and b % 2 == 0):
#     if (c % 2 == 0 and d % 2 > 0) or (c % 2 > 0 and d % 2 == 0):
#         print('YES')
#     else:
#         print('NO')
# elif (a % 2 > 0 and b % 2 > 0) or (a % 2 == 0 and b % 2 == 0):
#     if (c % 2 > 0 and d % 2 > 0) or (c % 2 == 0 and d % 2 == 0):
#         print('YES')
#     else:
#         print('NO')

# Хід короля
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (a - 1) <= c <= (a + 1) and (b - 1) <= d <= (b + 1):
#     print('YES')
# else:
#     print('NO')

# Хід тури
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if a == c or b == d:
#     print('YES')
# else:
#     print('NO')

# Хід слона
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (a - c == b - d) or (a + b == c + d):
#     print('YES')
# else:
#     print('NO')

# Хід коня
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (a - 1 == c) and (2 + b == d or b - 2 == d):
#     print('YES')
# elif (a + 1 == c) and (2 + b == d or b - 2 == d):
#     print('YES')
# elif (a - 2 == c) and (1 + b == d or b - 1 == d):
#     print('YES')
# elif (a + 2 == c) and (1 + b == d or b - 1 == d):
#     print('YES')
# else:
#     print('NO')

# Хід королеви
# a, b, c, d = int(input()), int(input()), int(input()), int(input())
# if (a - c == b - d) or (a + b == c + d) or a == c or b == d:
#     print('YES')
# else:
# print('NO')
