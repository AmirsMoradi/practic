import numpy as np

arr = np.array([[[10, 20, 30],
                 [40, 50, 60],
                 [70, 80, 90]]])

print(arr[0,1,2])
result = arr[0, 1:3, 1:3]
print(result)
print(arr.shape)