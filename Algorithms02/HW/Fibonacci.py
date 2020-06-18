# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# The task is to display all the numbers from start to n of the Fibonacci sequence φn

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2


# recursion works slow with large numbers. Even '35' takes a while
def fibonacci_recursion(n):
    if n < 0: raise ValueError("n must be > 0")
    if n == 0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fibonacci_recursion(n - 1) + fibonacci_recursion(n - 2)


for i in range(6):
    print(f'{i}: {fibonacci_recursion(i)}')

print(f'35: {fibonacci_recursion(35)}\n')


# another way, works faster
def fibonacci_faster(n):
    if n < 0: raise ValueError("n must be > 0")
    fn_1 = 0
    fn_2 = 1
    if n == 0: return fn_1
    elif n == 1: return fn_2
    else:
        for j in range(2, n + 1):
            fn = fn_1 + fn_2
            fn_1 = fn_2
            fn_2 = fn
        return fn_2


for i in range(6):
    print(f'{i}: {fibonacci_faster(i)}')

print(f'35: {fibonacci_faster(35)}')



