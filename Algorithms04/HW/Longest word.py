def longest_word(string):
    string = string.split()
    return max(string, key=len)


print(longest_word('  012 3456 098765 65'))


def longest_word_loop(string):
    string = string.split()
    max_s = 0
    result = ''
    for s in string:
        if len(s) > max_s:
            max_s = len(s)
            result = s
    return result


print(longest_word_loop('  012 3456 098765 65'))
