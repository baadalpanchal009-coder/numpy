# task 1
import numpy as np

arr = np.arange(1, 11)
print(arr)

# -------------------------------------------------------------------------------------

# task2
arr = np.arange(1, 11)

matrix = arr.reshape(2, 5)

print(matrix)

# --------------------------------------------------------------------------------------

# task3
import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

result = a * b

print(result)

# ------------------------------------------------------------------------------------------

# task 4
import numpy as np

arr = np.arange(1, 25).reshape(3, 4, 2)

print("Original Array:")
print(arr)

print("Indexing:")
print(arr[1, 2, 1])

print("Slicing:")
print(arr[0, :, :])

# ------------------------------------------------------------------------------------------

# task5
import numpy as np

arr = np.random.rand(3, 3)

print(arr)


# -----------------------------------------------------------------------------------------------

# task6
import numpy as np

a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print("Horizontal Stack:")
print(np.hstack((a, b)))

print("Vertical Stack:")
print(np.vstack((a, b)))

# --------------------------------------------------------------------------------------------