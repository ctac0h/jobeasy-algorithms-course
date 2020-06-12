year = int(input('Enter a year: '))
leap = False;
if year % 4 == 0:
    leap = True;
    if year % 100 == 0:
        leap = False
        if year % 400 == 0:
            leap = True


if leap:
    print(f"Year {year} is a leap year")
else:
    print(f"Year {year} is not a leap year")
