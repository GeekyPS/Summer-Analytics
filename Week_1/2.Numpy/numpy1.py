import numpy as np


# a python library for storing and doing operations on lists/arrays, and is much faster than lists/arrays

a = np.array([1,2,3])
b = np.array([[1,2,3],[9,9,2]])

c = np.zeros((5,5))
d = np.full((2,3),10) # all matrix element are 10

print(a)
print(b[1])
print('\n')
print(c)
print(d)


# random decimal numbers array of shape 4,3

print(np.random.rand(4,3))

# random integer values

print(np.random.randint(-1,7,size = (3,4)))

#identity matrix

print(np.identity(3))



# small task to make a given matrix

output = np.ones((5,5))

z = np.zeros((3,3))
z[1][1] = 9


output[1:4,1:4] = z

print(output)

copied_out = output.copy()
# this makes a copy of output array and assign it to copied_out , if straight way equality was used then it would have been passed by reference

copied_out = (copied_out*2) +1
# this operation is done element wise


print(copied_out)