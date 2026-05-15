import numpy as np 

# input vector 
x = np.array([1,2])

# weight matrix

W = np.array([  #Khi nhân thì nhân theo cột không phải theo hàng 
    [3,5],
    [4,6]
])

output = x @ W

print(output)
