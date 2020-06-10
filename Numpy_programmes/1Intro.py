import numpy as np

###################################### NUMPY BASICS ############################################
a = np.array([1,2,3,4,5])	# a normal numpy array
print(a)

b = [6,7,8,9,10]			# making numpy array from a python list
c = np.array(b)
print(b)

f = np.array([[1,2],[3,4],[5,6]])	# a normal 2d numpy array
print(f)

g = [[12,14],[16,18],[20,22]]		
h = np.array(g)						# making a 2d numpy array from a 2d python list
print(h)

i = [[12,14],[16,18,24],[20,22]]
j = np.array(i)
print(j)							# prints [list([12, 14]) list([16, 18, 24]) list([20, 22])]



print(f"The dimension of array {a} is {a.ndim}")	#ndim gives number of dimensions of the numpy array
print(f"The dimension of array {c} is {c.ndim}")
print(f"The dimension of array\n {f} is {f.ndim}")


print(f"The shape of the array {a} is {a.shape}")	#shape gives the shape of the numpy array
print(f"The shape of the array {c} is {c.shape}")
print(f"The shape of the array \n{f} is {f.shape}")


print(f"The type of the array {f} is {f.dtype}")	#dtype returns the data type of the numpy array

#We can specify the type of the data for our numpy array at the time of its creation

k = np.array([1,3,5] , dtype = 'int16')
print(f"The type of array {k} is {k.dtype}")


print(f"The size of the array {a} is {a.size}")	#size gives the total number of elements in the numpy array
print(f"The size of the array {c} is {c.size}")
print(f"The size of the array \n{f} is {f.size}")


print(f"The number of bytes used by array {a} is {a.nbytes}")	#nbytes gives the number of bytes used by numpy array
print(f"The number of bytes used by array {c} is {c.nbytes}")
print(f"The number of bytes used by array \n{f} is {f.nbytes}")
