# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b
# main.py

import assignment5demo2 #calculator

# Take user input
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("Addition:", assignment5demo2.add(a, b)) #calculator
print("Subtraction:", assignment5demo2.subtract(a, b)) #calculator
print("Multiplication:", assignment5demo2.multiply(a, b)) #calculator
print("Division:", assignment5demo2.divide(a, b)) #calculator