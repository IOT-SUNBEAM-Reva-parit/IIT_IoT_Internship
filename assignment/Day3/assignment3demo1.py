s = "hello world"
print(s.upper())
print(s.lower())
print(s.title())
print(s.capitalize())
print(s.swapcase())
s = "python programming"
print(s.find("pro"))
print(s.count("m"))
print(s.startswitch("py"))
print(s.endswitch("ing"))
a = "1234"
b = "python3"
c = "python"
print(a.isdigit())
print(b.isalnum())
print(c.isalpha())
print(c.islower())
s = "I like java"
print(s.replace("java","python"))
s  = "apple,mango,orange"
items = s.split(",")
print(items)
print(",".join(items))
s = "python"
print(s.strip())
print(s.istrip())
print(s.rstrip())
s = "python"
print(len(s))
print(s.center(10,"*"))
print(s.ijust(10,"-"))
print(s.rjust(10,"-"))
name = "Ravi"
age = 21
print("Name: {}, Age: {}".format(name, age))
print(f"Name: {name}, Age:{age}")