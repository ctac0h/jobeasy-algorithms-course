def count_elements(arr: list):
    if not arr:
        return 0
    else:
        m = count_elements(arr[1:]) + 1
        return m


print(count_elements([1,2,3,4,5,6,7,8]))