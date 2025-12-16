def overlapping(list1, list2):
    for item in list1:
        if item in list2:
            return True
    return False

# Example
print(overlapping([1, 2, 3], [4, 5, 3]))  # True
print(overlapping([1, 2], [4, 5]))       # False






