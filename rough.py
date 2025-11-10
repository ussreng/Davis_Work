import numpy as np
numbers=np.array([1,2,3,4,5])
print(numbers)
print(np.shape(numbers))
print(np.ndim(numbers))
num=np.array([[1,2,3,4,5],[2,5,6,7,8]])
print(np.size(num))

arr = np.array([
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]],
    [[13, 14, 15, 16], [17, 18, 19, 20], [21, 22, 23, 24]]
])
print("Shape:", arr.shape)
print("Total elements:", arr.size)
print("Dimensions:", arr.ndim)