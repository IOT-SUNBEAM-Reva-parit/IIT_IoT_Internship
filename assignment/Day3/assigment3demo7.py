def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)


num = int(input("Enter a number for factorial: "))
print("Factorial =", factorial(num))

base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
print("Power =", power(base, exponent))
        