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


# Test
print()
print("Homework test")
print()


for i in range(5):
    rand_num = randint(0, 99999999)
    print('sum_of_digits_string')
    print(f'Random number is: {rand_num}\n'
          f'The sum of it\'s digits is: {sum_of_digits_string(rand_num)}')
    print('sum_of_digits_no_string')
    print(f'Random number is: {rand_num}\n'
          f'The sum of it\'s digits is: {sum_of_digits_no_string(rand_num)}\n')