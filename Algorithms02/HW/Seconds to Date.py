# Write a Python program to convert seconds to day, hour, minutes and seconds.
import datetime


def seconds_to_date(secs):
    date = datetime.timedelta(seconds=secs)
    return date


print(seconds_to_date(100))
print(seconds_to_date(360))
print(seconds_to_date(3600))
print(seconds_to_date(7287))
