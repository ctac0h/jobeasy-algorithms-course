one = int(input("Enter 1'st number: "))
two = int(input("Enter 2'nd number: "))
three = int(input("Enter 3'rd number: "))


def print_number(num):
    print(f'Largest number is {num}')


if one >= two and one >= three:
    print_number(one)

elif two >= three:
    print_number(two)

else:
    print_number(three)
