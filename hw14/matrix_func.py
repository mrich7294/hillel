from my_package import input_data as idd

from random import randint

from my_package import my_sort


def sort_to_matrix():
    """
    Функція запитує розмірність матриці, заповнює матрицю
    рандомними значеннями та сортує парні стовпці матриці за зростанням та
    непарні за спаданням значень
    """
    n = input('Введіть ціле число більше 4: ')
    n = idd.input_str_to_int(n)
    matrix = [
            [randint(0, 50) for _ in range(j, j + n)]
            for j in range(0, n)
    ]
    # print('Вихідні дані:')  # друкує вихідну матрицю
    # for m in matrix:
    #     print(m)

    lst_help = [0 for _ in range(0, n)]
    for i in range(0, n):  # пошук суми стовпців
        for j in range(0, n):
            lst_help[i] += matrix[j][i]
    matrix.append(lst_help)  # додавання суми стовпця до матриці
    matrix.append(n)
    # print(matrix)
    # print('Допоміжний список:\n', lst_help, '\n')  # друкує суми стовпців

    for i in range(len(lst_help)):
        n = i
        for j in range(i+1, len(lst_help)):
            if lst_help[j] < lst_help[n]:
                n = j
        lst_help[n], lst_help[i] = \
            lst_help[i], lst_help[n]
        for k in range(0, len(lst_help)):
            matrix[k][n], matrix[k][i] = \
                matrix[k][i], matrix[k][n]

    n = matrix[-1]
    matrix.pop(-1)
    for x in range(0, n):   # сортування всередині стовпців
        if x % 2 == 0:
            lst_help = [matrix[y][x] for y in range(0, n)]
            lst_help = my_sort.rock_sort(lst_help)
            for p in range(0, n):
                matrix[p][x] = lst_help[p]
        else:
            lst_help = [matrix[y][x] for y in range(0, n)]
            lst_help = my_sort.buble_sort(lst_help)
            for p in range(0, n):
                matrix[p][x] = lst_help[p]
    return matrix


def output_list(lst: list):
    """Функція виводить матрицю"""
    print('Відсортована матриця:')
    for m in lst:
        for k in range(len(m)):
            elem = m[k]
            print(f'{elem:^5}', end='')
        print()
    return output_list


if __name__ == "__main__":
    output_list(sort_to_matrix())
