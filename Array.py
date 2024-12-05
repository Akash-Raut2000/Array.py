from array import array

# Create an integer array
a = array('i', [1, 2, 3])

# Print the array
print("Array:", a)

# Access and modify elements
print("First element:", a[0])
a[1] = 42
print("Modified array:", a)

# Append and remove elements
a.append(99)
print("After append:", a)
a.remove(42)
print("After removal:", a)


