from random import randint


def selection_by_key(lst: list, key):
    print(lst)
    key_value_list = [e.get(key) for e in lst]
    print(key_value_list)
    i = 0
    while i < len(key_value_list):
        a = min(key_value_list[i:])
        min_index = key_value_list.index(a)
        key_value_list[i], key_value_list[min_index] = key_value_list[min_index], key_value_list[i]
        lst[i], lst[min_index] = lst[min_index], lst[i]
        i += 1
    print([e.get(key) for e in lst])
    print(lst)
    return lst


def get_random_dict(k1, k2):
    return {k1: randint(-100, 100), k2: randint(-100, 100)}


def get_list_of_dict(l):
    k1 = "key1"
    k2 = "key2"
    return [get_random_dict(k1, k2) for i in range(l)]


my_dict = (get_list_of_dict(5))

selection_by_key(my_dict,'key1')




