import numpy as np

list1=[0,1,2,3,4]
arr1d=np.array(list1)
print(type(arr1d))
#<class 'numpy.ndarray'>
print(arr1d)
#array([0, 1, 2, 3, 4])
#  list1+2
# Traceback (most recent call last):
#   File "<pyshell#5>", line 1, in <module>
#     list1+2
# TypeError: can only concatenate list (not "int") to list
arr1d+1
#array([1, 2, 3, 4, 5])
list2=[[0,1,2],[3,4,5],[6,7,8,]]
arr2d=np.array(list2)
print(arr2d)
# array([[0, 1, 2],
#        [3, 4, 5],
#        [6, 7, 8]])
arr2d_f=np.array(list2,dtype='float')
print(arr2d_f)
# array([[0., 1., 2.],
#        [3., 4., 5.],
#        [6., 7., 8.]])
arr2d_f.astype('int').astype('str')
# array([['0', '1', '2'],
#        ['3', '4', '5'],
#        ['6', '7', '8']], dtype='<U11')

print('Shape:', arr2d.shape)
#Shape: (3, 3)
print('Dataype:', arr2d.dtype)
#Dataype: int32
print('Size:',arr2d.size)
#Size: 9
print('Num Dimension:',arr2d.ndim)
#Num Dimension: 2