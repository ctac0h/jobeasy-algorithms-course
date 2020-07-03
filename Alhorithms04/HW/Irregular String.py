import re


def to_regular_string(string):
    string = string.split()
    result = ''
    for s in string:
        result += s + ' '
    return result.strip()


print(to_regular_string('   wdfsdf sdfsdf     sdf sdf   sdgf      sdg sdg sdgsdgsgd    '))


def to_regular_string_join(string):
    return " ".join(string.split())


print(to_regular_string_join('   wdfsdf sdfsdf     sdf sdf   sdgf      sdg sdg sdgsdgsgd    '))


def to_regular_string_regex(string):
    return re.sub(' +', ' ', string).strip()


print(to_regular_string_regex('   wdfsdf sdfsdf     sdf sdf   sdgf      sdg sdg sdgsdgsgd    '))


def to_regular_string_long_way(string):
    result = ''
    space = True
    for i, ch in enumerate(string):
        if ch == ' ':
            if space or i == len(string)-1:
                continue
            else:
                result += ' '
                space = True
        else:
            result += ch
            space = False
    return result


print(to_regular_string_long_way('   wdfsdf sdfsdf     sdf sdf   sdgf      sdg sdg sdgsdgsgd    '))




