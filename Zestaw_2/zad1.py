from math import sqrt

n = int(input())
a1, a2 = 1, 2
b1, b2 = 1, 2

while a1 <= n:
    while b1 <= n:
        if a1 * b1 == n:
            print(True)
            exit()
        b1, b2 = b2, b1 + b2
    a1, a2 = a2, a1 + a2
    b1, b2 = a1, a2
print(False)

