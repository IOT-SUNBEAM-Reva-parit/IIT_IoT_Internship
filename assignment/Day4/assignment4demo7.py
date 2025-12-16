 # Matrix as list of lists (3x4)
matrix_list = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

# Matrix as tuple of tuples (3x4)
matrix_tuple = (
    (12, 11, 10, 9),
    (8, 7, 6, 5),
    (4, 3, 2, 1)
)

# Function to calculate addition and subtraction
def matrix_add_sub(mat1, mat2):
    addition = []
    subtraction = []

    for i in range(3):
        add_row = []
        sub_row = []
        for j in range(4):
            add_row.append(mat1[i][j] + mat2[i][j])
            sub_row.append(mat1[i][j] - mat2[i][j])
        addition.append(add_row)
        subtraction.append(sub_row)

    return addition, subtraction

# Main
add_result, sub_result = matrix_add_sub(matrix_list, matrix_tuple)

# Printing results
print("Addition Result Matrix:")
for row in add_result:
    print(row)

print("\nSubtraction Result Matrix:")
for row in sub_result:
    print(row)