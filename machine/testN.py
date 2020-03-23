#testing the use of numpy to manipulate arrays, matrix and vectors
#as you progress uncommet the print statements to see the outpus

import numpy as nm

#application of Broadcasting
#a has a shape of 3

a = nm.array([1,2,3])

#b has a shap of 2

b = nm.array([4,5])

#to compute the outer product, we reshape a to be a column
#vectot of shape(3,1); we can then broadcast it against b to yield 
#an output of shape(3,2), which is the outer product of a and b
#
# print(nm.reshape(a,(3,1))*b)

#add a vector to each row of the matrix

c = nm.array([[1,2,3],[4,5,6]])

#c has shape (2,3) and v has shape(3,) so they hroadcast to (2,3)

#print(c + a)

#add a vector to each column of a matrix
# c has shape(2,3) and b has shape(2,).
#if we transpose c then it has shape (3,2) and can be broadcast
#against b to yield a resukt of shape (3,2); transposing this result
#yield the final resukt of shape(2,3) which is the matrix c with
#the vector b added to each column

#print((c.T + b).T)

#you can also reshape b to be a row vector osf shape(2,1);
#the broadcast it directly against c to produce the same output

#print(c + nm.reshape(b,(2,1)))

#Multiply a matrix by a constant:
#c has shape (2,3). numpy treats scalar as arrays of shape();
#these can be broadcast together to shape (2,3), producing the an array

print(c*2)