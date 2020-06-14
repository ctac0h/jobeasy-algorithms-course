from random import randint


def sum_of_digits_string(num):
    if num < 0:
        return None
    result = 0
    for char in str(num):
        result += int(char)
    return result


def sum_of_digits_no_string(num):
    if num < 0:
        return None
    result = 0
    while num > 0:
        result += num % 10
        num = num // 10
    return result


def get_random_int_with_n_digits_v1(n):
    return randint(10 ** (n-1), 10 ** n-1)


def get_random_int_with_n_digits_v2(n):
    return int("".join([str(randint(0,10)) for j in range(n)]))


# Test
print("\nHomework test\n")

digits = int(input('Enter a number of digits: '))
tests = int(input('Enter number of tests: '))
if digits < 1:
    digits = 1
if tests < 1:
    tests = 1


for i in range(tests):
    rand_num = get_random_int_with_n_digits_v1(digits)
    print('\nsum_of_digits_string')
    print(f'Random number is: {rand_num}\n'
          f'The sum of it\'s digits is: {sum_of_digits_string(rand_num)}')
    print('sum_of_digits_no_string')
    print(f'Random number is: {rand_num}\n'
          f'The sum of it\'s digits is: {sum_of_digits_no_string(rand_num)}')