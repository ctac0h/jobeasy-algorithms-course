# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


def get_digital_root_easy_way(number):
    if number <= 0:
        return 0
    while number // 10 != 0:
        number = sum_of_digits_string(number)
    return number


def sum_of_digits_string(num):
    if num < 0:
        return None
    result = 0
    for char in str(num):
        result += int(char)
    return result


def get_digital_root_all_in_one(number):
    if number <= 0:
        return 0
    while number // 10 != 0:
        result = 0
        while number > 0:
            result += number % 10
            number = number // 10
        number = result
    return number


def get_digital_root_smarty_pants_edition(number):
    if number <= 0:
        return 0
    if number % 9 == 0:
        return 9
    else:
        return number % 9


print(get_digital_root_all_in_one(16))
print(get_digital_root_all_in_one(942))
print(get_digital_root_all_in_one(132189))
print(get_digital_root_all_in_one(493193))
print(get_digital_root_all_in_one(333333))
print(get_digital_root_all_in_one(333333))
print()
print(get_digital_root_smarty_pants_edition(16))
print(get_digital_root_smarty_pants_edition(942))
print(get_digital_root_smarty_pants_edition(132189))
print(get_digital_root_smarty_pants_edition(493193))
print(get_digital_root_smarty_pants_edition(333333))
print(get_digital_root_smarty_pants_edition(999999))
