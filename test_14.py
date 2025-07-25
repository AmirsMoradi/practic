import numpy as np

arr = np.array([
    [[11, 12, 13],
     [14, 15, 16],
     [17, 18, 19]],

    [[21, 22, 23],
     [24, 25, 26],
     [27, 28, 29]]
])

print(arr[1,1,2])
print(arr[0,1])
print(arr[1,:,0:1])
print(arr[0, 1:3, 1:3])