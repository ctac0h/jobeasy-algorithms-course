def is_even(num):
    if num % 2 == 0:
        return True
    return False


def count_even_odd(num):
    evens = 0
    odds = 0

    for digit in str(num):
        if is_even(int(digit)):
            evens += 1
        else:
            odds += 1
    return evens, odds


n = int(input("Enter a number: "))
result = count_even_odd(n)
print(f"Evens: {result[0]}\nOdds: {result[1]}")