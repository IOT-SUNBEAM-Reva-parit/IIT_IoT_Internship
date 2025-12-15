 def print_binary(n):
    if n == 0:
        print(0)
    else:
        binary = ""
        while n > 0:
            binary = str(n % 2) + binary
            n = n // 2
        print(binary)

# Example usage
num = int(input("Enter a number: "))
print("Binary format:")
print_binary(num)