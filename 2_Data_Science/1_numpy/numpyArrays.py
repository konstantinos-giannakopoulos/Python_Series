import numpy as np

'''
1) Creating arrays
'''
print("\n--- 1) Creating Arrays ---")
a = np.array([10, 20, 30])
b = np.array([1, 77, 2, 3])

print(a[0])
print(b)

# 2d array
multidim_a = np.array([
    [10, 11, 12],
    [20, 21, 22]
    ])
print(multidim_a[1][2])

#3d array -> 3x3x4 (shape) matrix
matrix_a = np.array([
    [
        [10, 20, 30, 40],
        [50, 60, 70, 80],
        [3, 5, 7, 1]
    ],
    [
        [9, 19, 2, 39],
        [1, 2, 3, 3],
        [0, 4, 9, 3]
    ],
    [
        [72, 3, 8, 1],
        [32, 1, 22, 2],
        [0, 2, 3, 1]
    ]
],dtype=float)

print(matrix_a)
print('Shape: ', matrix_a.shape)
print('No dimensions: ', matrix_a.ndim)
print('Size: ', matrix_a.size)
print('Data type: ', matrix_a.dtype)



'''
2) Filling arrays
'''
print("\n--- 2) Filling Arrays ---")
a_fill = np.full((3,5,4), 7)
print(a_fill)

a_fill_zeros = np.zeros((3,3))
a_fill_ones = np.ones((2,3,4,2))
print(a_fill_zeros)
print(a_fill_ones)

a_empty = np.empty((4,4))
a_random = np.random.random((2,3))
print(a_empty)
print(a_random)

a_range  = np.arange(10, 50, 5)
print(a_range)
a_linspace = np.linspace(0, 100, 11)
print(a_linspace)


'''
3) Attributes of arrays
'''
print("\n--- 3) Attributes of Arrays ---")
#Aggregate functions
print(matrix_a.max())
print(matrix_a.min())
print(matrix_a.mean())
print(np.median(matrix_a))
print(np.std(matrix_a))

'''
4) Manipulating Arrays
'''
print("\n--- 4) Manipulating Arrays ---")
#Shape
print(multidim_a)
print(multidim_a.shape)
print(multidim_a.reshape(3,2))
print(multidim_a.flatten())
print(multidim_a.transpose())
for x in multidim_a.flat:
    print(x)
print('flat.. ', multidim_a.flat[2])
#Join
print(np.concatenate((multidim_a, multidim_a)))
print(np.stack((multidim_a, multidim_a)))
#Split
print(np.hsplit(multidim_a,3))
print(np.vsplit(multidim_a,2))

#Adding and Removing
print(np.append(multidim_a,[1,1,1]))

#Loading and Saving
print("\n>>> Loading and Saving")
np.save('matrix_a.npy', matrix_a)
loadedArray =  np.load('matrix_a.npy')
print(loadedArray)

# CSV
np.savetxt('matrix_a.csv', a)
loadedArrayCSV =  np.loadtxt('matrix_a.csv')
print(loadedArrayCSV)
