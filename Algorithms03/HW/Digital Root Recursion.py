
def digital_root(num):
    if num < 9:
        return num
    else:
        return digital_root(sum(int(digit) for digit in str(num)))


print(digital_root(10101))
