from random import randint


def insertion(lst: list):
    print(lst)
    for i in range(1, len(lst)):
        j = i - 1
        temp = lst[i]
        while lst[j] > temp and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
        print(lst)


def get_random_list(length: int):
    return [randint(-99, 99) for i in range(length)]


insertion(get_random_list(5))