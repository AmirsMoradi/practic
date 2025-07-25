import numpy as np

arr = np.array([
    [[11, 12, 13],
     [14, 15, 16],
     [17, 18, 19]],

    [[21, 22, 23],
     [24, 25, 26],
     [27, 28, 29]],

    [[31, 32, 33],
     [34, 35, 36],
     [37, 38, 39]]
])



print(arr.shape)
print(arr[0,1])
print(arr[1,2:3,1:2])
print(arr[0,1])
result = [arr[i, 1, 0] for i in range(arr.shape[0])]
print(result)
print(arr[1,1:3,2:3])
for i  in range(arr.shape[0]):
    print(np.trace(arr[i]))



for i in range(arr.shape[0]):
    for j in range(arr.shape[1]):
        for k in range(arr.shape[2]):
            if arr[i, j, k] % 3 == 0:
                print(arr[i, j, k])



ansewr =[arr[i,0,2]for i in range(arr.shape[0])]
print(np.trace(arr[ansewr]))
