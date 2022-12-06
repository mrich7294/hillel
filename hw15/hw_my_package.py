import random
import time
from my_package.sort import *

if __name__ == "__main__":
    n = 5000
    lst = [random.randint(0, 50) for _ in range(0, n)]
    # print(lst)
    t1 = time.time()
    my_sort.selection_sort(lst)
    t2 = time.time()
    print('Sorting execution time for selection_sort = ', t2 - t1)
    # print(f'Sorting execution time for selection_sort = {t2 - t1}\n{lst}')
    t1 = time.time()
    my_sort.buble_sort(lst)
    t2 = time.time()
    print('Sorting execution time for buble_sort = ', t2 - t1)
    # print(f'Sorting execution time for buble_sort = {t2 - t1}\n{lst}')
    t1 = time.time()
    my_sort.rock_sort(lst)
    t2 = time.time()
    print('Sorting execution time for rock_sort = ', t2 - t1)
    # print(f'Sorting execution time for rock_sort = {t2 - t1}\n{lst}')
