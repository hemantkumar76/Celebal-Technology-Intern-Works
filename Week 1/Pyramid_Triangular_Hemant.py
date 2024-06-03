# Pyramid Triangle Wala Solved by Hemant
def pyramid_wala(n):
    for i in range(1, n + 1):
        print(' ' * (n - i) + '*' * (2 * i - 1))


# number of rows dalenege
n = 10
pyramid_wala(n)
