from random import randint


def insertion_key(lst: list, key):
    print(lst)
    for i in range(1, len(lst)):
        j = i - 1
        temp = lst[i]
        while lst[j].get(key) > temp.get(key) and j >= 0:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = temp
    print(lst)


def get_random_dict(k1, k2):
    return {k1: randint(-100, 100), k2: randint(-100, 100)}


def get_list_of_dict(l):
    k1 = "key1"
    k2 = "key2"
    return [get_random_dict(k1, k2) for i in range(l)]


insertion_key(get_list_of_dict(5), 'key1')