
n = int(input('Enter a number: '))


def factorial(num):
    if num < 0:
        return None
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


print(factorial(n))
