import numpy as np

arr = np.random.randint(0, 10, size = 10)
print("arr", arr)
print("mean", np.mean(arr))
print("max", np.max(arr))
print("min", np.min(arr))
print("sum", np.sum(arr))
print("sort", np.sort(arr))
print("shuffled", np.random.permutation(arr))
print("squared", np.square(arr))
print("square root", np.sqrt(arr))  
