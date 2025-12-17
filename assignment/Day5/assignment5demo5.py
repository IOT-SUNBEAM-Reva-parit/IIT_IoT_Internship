
def add(a, b):

    return a + b

def multiply(a, b):
   
    return a * b


def reverse_string(s):
    
    return s[::-1]

def count_vowels(s):
  
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count


print("--- Demonstration ---")


num1 = 10
num2 = 5

print(f"Addition: {num1} + {num2} = {add(num1, num2)}")
print(f"Multiplication: {num1} * {num2} = {multiply(num1, num2)}")

print("-" * 20)


text = "Hello World"
print(f"Original String: '{text}'")

print(f"Vowel Count: {count_vowels(text)}")