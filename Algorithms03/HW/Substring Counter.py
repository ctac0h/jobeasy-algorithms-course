# Write a Python function, which will count how many times a character is included in a string.
# DON’T USE METHOD COUNT


def char_count(string, char):
    counter = 0
    for ch in string:
        if ch == char:
            counter += 1
    return counter


def substring_count(string, sub):
    count = 0
    sub_len = len(sub)
    i = 0
    while i < len(string):
        if string[i:i+sub_len] == sub:
            count += 1
            i += sub_len
            continue
        i += 1
    return count


print(substring_count('aabaaaabaaaa', 'aa'))