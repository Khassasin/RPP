import numpy as np

arr = np.random.randint(-100, 100, 10)

print(arr)

min_num = arr[0]
for i in arr:
    if i < min_num:
        min_num = i

print(min_num)
