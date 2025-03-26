# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):
    if not numbers:
        return None, None

    unique_numbers = sorted(list(set(numbers)), reverse=True)

    if len(unique_numbers) == 1:
        return unique_numbers[0], None

    return unique_numbers[0], unique_numbers[1]
    
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
max_val, second_max_val = max_two_in_list(numbers)
print(f"Max: {max_val}, Second Max: {second_max_val}")

# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):
    return sorted(list(set(numbers)))

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
result = remove_duplicates_and_sort(numbers)
print(result)

# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):
    cumulative = []
    current_sum = 0
    for num in arr:
        current_sum += num
        cumulative.append(current_sum)
    return cumulative

arr = [1, 2, 3, 4, 5]
result = cumulative_sum(arr)
print(result)

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0

    transpose = [[0 for _ in range(rows)] for _ in range(cols)]

    for i in range(rows):
        for j in range(cols):
            transpose[j][i] = matrix[i][j]

    return transpose

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result = transpose_matrix(matrix)
print(result)

# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):
    return lst[::step]

lst = [2, 4, 6]
step = 3
result = slice_every_nth(lst, step)
print(result)

# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must have the same length for dot product")

    return sum(x * y for x, y in zip(list1, list2))

list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = dot_product(list1, list2)
print(result)

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0])
    rows2 = len(matrix2)
    cols2 = len(matrix2[0])

    if cols1 != rows2:
        raise ValueError("Matrices cannot be multiplied")

    result = [[0 for _ in range(cols2)] for _ in range(rows1)]

    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result

matrix1 = [[1, 2], [3, 4]]
matrix2 = [[5, 6], [7, 8]]
result = matrix_multiplication(matrix1, matrix2)
print(result)
