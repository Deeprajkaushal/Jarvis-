import numpy as np

# array=np.array([1,2,3,4,5])
# array2=array*2
# print(array2)

# array=np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(array.ndim)
# print(array.shape)
# print(array.size)

a1=np.array([[1,2,3]])
a2=np.array([[4],[5],[6]])

print(a1.shape)
print(a2.shape)

multiply=a1*a2
print(multiply)

print(np.sum(a1 + a2))