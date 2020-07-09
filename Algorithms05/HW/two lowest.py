def two_lowest(arr):
    result = []
    for x in range(2):
        result.append(min(arr))
        arr.remove(min(arr))
    return result


print(two_lowest([1,2,3,4,5,6,7]))
print(two_lowest([1,2,3,4,1,6,7]))
print(two_lowest([-1,-2,-3,-4,-5,-6,-7]))
print(two_lowest([-1,-7,-3,-4,-5,-6,-7]))