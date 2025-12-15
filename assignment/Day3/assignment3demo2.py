s = input("Enter a string:")
print("First 5 characters:",s[0:5])
print("from index 2 to 6:",s[2:6])

s = input("Enter a string:")
print("from start to index 4:",s[:4])
print("from index 3 to end:",s[3:])

s = input("Enter a string:")
print("last 3 characters:",s[-3:])
print("without last 2 characters:",s[:-2])

s = input("Enter a string:")
print("Every second characters:",s[::2])
print("Every third character:",s[::3])

s = input("Enter a string:")
print("reversed string:",s[::-1])

s = input("Enter a string:")
print("Alternate characters:",s[1::2])

s = input("Enter a string:")
startn= int(input("Enter start index:"))
end = int(input("Enter end index:"))
print("sliced string",s[start:end])





