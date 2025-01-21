a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(a[::-1][::2] + a[::-1][1::2])



# list comprehension
# SYNTAX - [expression for item in iterable if condition]
# For example, let's say we want to create a list of squares of numbers from 0 to 9
# We can do this using list comprehension as follows:
squares = [x**2 for x in range(10)]
# print(squares)

mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# flatten the matrix
flattened = [num for row in mat for num in row]
# print(flattened)

x, *middle, z = a
# print(x, z)