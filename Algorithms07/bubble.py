from random import randint


def bubble(lst: list):
    print(lst)
    for i in range(len(lst)):
        j = 0
        while j < len(lst)-1:
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
            j += 1
    print(lst)
    return lst





def get_random_list(length: int):
    return [randint(-99, 99) for i in range(length)]


bubble(get_random_list(5))