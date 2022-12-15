

def buble_sort(list_to_sort: list) -> list:
    """Sort to list buble to up"""
    n = len(list_to_sort)
    for i in range(n):
        for j in range(n-2, i-1, -1):
            if list_to_sort[j] > list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j + 1] = \
                    list_to_sort[j+1], list_to_sort[j]
    return list_to_sort


def rock_sort(list_to_sort: list) -> list:
    """Sort to list rock to down"""
    n = len(list_to_sort)
    for i in range(n):
        for j in range(n-1-i):
            if list_to_sort[j] < list_to_sort[j+1]:
                list_to_sort[j], list_to_sort[j + 1] = \
                    list_to_sort[j+1], list_to_sort[j]
    return list_to_sort


def selection_sort(list_to_sort: list) -> list:
    """Sort to list selection method to up"""
    for i in range(len(list_to_sort)):
        minimum = i
        for j in range(i+1, len(list_to_sort)):
            if list_to_sort[j] < list_to_sort[minimum]:
                minimum = j
        list_to_sort[minimum], list_to_sort[i] = \
            list_to_sort[i], list_to_sort[minimum]
    return list_to_sort


if __name__ == "__main__":
    pass
