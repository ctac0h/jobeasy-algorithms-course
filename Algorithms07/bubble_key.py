from random import randint


def bubble_key(lst: list, key):
    print(lst)
    for i in range(len(lst)):
        j = 0
        while j < len(lst)-1:
            if lst[j].get(key) > lst[j+1].get(key):
                lst[j], lst[j+1] = lst[j+1], lst[j]
            j += 1
    print(lst)
    return lst



def get_random_dict(k1, k2):
    return {k1: randint(-100, 100), k2: randint(-100, 100)}


def get_list_of_dict(l):
    k1 = "key1"
    k2 = "key2"
    return [get_random_dict(k1, k2) for i in range(l)]


bubble_key(get_list_of_dict(5), 'key1')
