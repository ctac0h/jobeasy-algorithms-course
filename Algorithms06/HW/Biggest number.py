def biggest_number(arr: list):
    if not arr:
        return 0
    else:
        m = biggest_number(arr[1:])
        return m if m > arr[0] else arr[0]


