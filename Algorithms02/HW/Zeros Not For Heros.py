# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
#
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway


def get_rid_of_zeros(number):
    if number == 0:
        return 0
    while number % 10 == 0:
        number = number // 10
    return number


def get_rid_of_zeros_str(number):
    if number == 0:
        return 0
    return int(str(number).strip('0'))


print(get_rid_of_zeros(1450))
print(get_rid_of_zeros(960000))
print(get_rid_of_zeros(1050))
print(get_rid_of_zeros(-1050))
print(get_rid_of_zeros(0))

print(get_rid_of_zeros_str(1450))
print(get_rid_of_zeros_str(960000))
print(get_rid_of_zeros_str(1050))
print(get_rid_of_zeros_str(-1050))
print(get_rid_of_zeros_str(0))
