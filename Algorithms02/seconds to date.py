# Write a Python program to convert seconds to day, hour, minutes and seconds.


def sec_to_hms(seconds):
    hours = seconds // 3600
    seconds = seconds - hours * 3600
    minutes = seconds // 60
    seconds = seconds - minutes * 60
    return f'{hours}:{minutes}:{seconds}'


print(sec_to_hms(10121))


# TODO Use datetime library to solve problem Seconds to Date