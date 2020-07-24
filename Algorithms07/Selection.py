from random import randint


def selection_sort(lst: list):
    for i, _ in enumerate(lst):
        min_index = i
        for j in range(i + 1, len(lst)):
            if lst[min_index] > lst[j]:
                min_index = j
        lst[i], lst[min_index] = lst[min_index], lst[i]
    return lst


def selection_sort_another(lst):
    print(lst)
    i = 0
    while i < len(lst):
        a = min(lst[i:])
        min_index = lst.index(a)
        lst[i], lst[min_index] = lst[min_index], lst[i]
        i += 1
    print(lst)
    return lst


def sort(lst):
    for i in range(len(lst)//2):
        a = min(lst[i:len(lst)-i])
        b = max(lst[i:len(lst)-i])
        index_a = lst.index(a)
        index_b = lst.index(b)
        lst[index_a], lst[i], lst[index_b], lst[-1 - i] = lst[i], lst[index_a], lst[-1-i], lst[index_b]
    return lst


def get_random_list(length: int):
    return [randint(-99, 99) for i in range(length)]


selection_sort(get_random_list(6000))

# selection_sort_another(get_random_list(6))

