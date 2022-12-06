import random
import time
from my_package.sort import *

if __name__ == "__main__":
    lst = [random.randint(0, 50) for _ in range(0, 5000)]
    # print(lst)
    t1 = time.time()
    my_sort.selection_sort(lst)
    t2 = time.time()
    print('selection_sort = ', t2 - t1)
    t1 = time.time()
    my_sort.buble_sort(lst)
    t2 = time.time()
    print('buble_sort = ', t2 - t1)
    t1 = time.time()
    my_sort.rock_sort(lst)
    t2 = time.time()
    print('rock_sort = ', t2 - t1)

