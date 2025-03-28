import numpy as np
arr=np.array([[2,5,7],[32,45,56],[29,81,54]])
print(arr)

mean = np.mean(arr)
print(f"Mean is {mean}")
median = np.median(arr)
print(f"Median is {median}")
std = np.std(arr)
print(f"Std is {std}")

sum = np.sum(arr)
print(f"Total sum is {sum}")

reshaped = arr.reshape(9,1)
print(reshaped)