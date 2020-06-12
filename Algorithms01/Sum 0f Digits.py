from random import randint


random_3_digit_number = randint(100, 999)


def sum_of_digits_lesson(num):
    ones = num % 10
    tens = num // 10 % 10
    hundreds = num // 100
    return ones + tens + hundreds


print(f'Random number is: {random_3_digit_number}\n'
      f'The sum of it\'s digits is: {sum_of_digits_lesson(random_3_digit_number)}')




