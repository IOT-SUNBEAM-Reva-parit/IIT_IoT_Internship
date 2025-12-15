def add(a,b):
    return a + b

def sub(a,b):
    return a - b

def mul(a,b):
    return a * b

def div(a,b):
    if b == 0:
        return "Error Divisin by Zero"
    return a / b
while True:
    print("\n---Arithmetic Operation Menu---")
    print("1.Addition")
    print("2.substraction")
    print("3.multipliction")
    print("4.division")
    print("5.Exit")
    choice = int(input("Enter your choice:"))
    if choice == 5:
        print("Program terminated")
        break
    a = float(input("Enter first number:"))
    b = float(input("Enter second number:"))
    if choice == 1:
        print("Result:", add(a,b))
    elif choice == 2:
        print("Result:", sub(a,b))
    elif choice == 3:
        print("Result:", mul(a,b))
    elif choice == 4:
        print("Result:", div(a,b))
    else:
        print("Invalid choice! Try again.")
        
    



