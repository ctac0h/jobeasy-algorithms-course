"""Find and replace a substring in a string for another substring.
User enter from a keyboard a string and both substrings. """

user_string = input("Enter a string: ")
user_find_str = input("Enter what to replace: ")
user_replace_str = input("Enter how to replace: ")


def replace(string, find_str, replace_str):
    result = ''
    i = 0
    find_str_len = len(find_str)

    while i < len(string):
        if string[i:i + find_str_len] == find_str:
            result += replace_str
            i += find_str_len
        else:
            result += string[i]
            i += 1
    print(result)
    return result


replace(user_string, user_find_str, user_replace_str)
"""
replace('Look at my horse, my horse is amazing', 'horse', 'tractor')
replace('aaaaaa', 'aa', 'b')
replace('aaaaaa', 'a', 'bb')
"""