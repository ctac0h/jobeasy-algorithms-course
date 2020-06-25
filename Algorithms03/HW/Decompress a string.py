# TODO: Write a function for decompressing string “a4b3c2d”
import re


def decompress_string(string):
    result = ''
    char = ''
    count = ''
    s_len = len(string)

    for i in range(s_len):
        if string[i].isalpha():
            if count != '':
                result += char * (int(count) - 1)
                count = ''
            char = string[i]
            result += char
        else:
            count += string[i]
            if i == s_len-1:
                result += char * (int(count) - 1)
    return result


print(decompress_string('a4b3c2d'))


def decompress_string_regex(string):
    result = ''
    regex = re.compile('[A-z]\d*')
    sub_strings = regex.findall(string)
    for elem in sub_strings:
        if len(elem) == 1:
            result += elem
        else:
            result += elem[0] * int(elem[1:])

    print(result)
    return result


decompress_string_regex('a4b3c2d')