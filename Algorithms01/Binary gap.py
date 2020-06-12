n = int(input('Enter a number: '))


def to_bin(num):
    bin_string = ''
    while num > 0:
        bin_string += str(num % 2)
        num = num // 2
    return bin_string[::-1]


def binary_gap(bin_num):
    max_gap = 0
    counter = 0

    for digit in bin_num:
        if digit == '1':
            if max_gap < counter:
                max_gap = counter
            counter = 0
        else:
            counter +=1
    return max_gap


print(binary_gap(to_bin(n)))