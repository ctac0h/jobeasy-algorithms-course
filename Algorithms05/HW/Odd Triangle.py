"""
                1                       (1)     1*1*1
            3         5                 (8)     2*2*2
        7       9       11              (27)    3*3*3
    13      15      17      19          (64)    4*4*4
21      23      25      27      29      (125)   5*5*5


1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16
"""


def sum_of_odd_triangle_row(row):
    return row ** 3


print(sum_of_odd_triangle_row(1))
print(sum_of_odd_triangle_row(2))
print(sum_of_odd_triangle_row(3))
print(sum_of_odd_triangle_row(4))
print(sum_of_odd_triangle_row(5))
