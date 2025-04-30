def power(a, b):
    if b == 0:
        return 1
    return a * power(a, b - 1)

print("3^4 =", power(3, 4))