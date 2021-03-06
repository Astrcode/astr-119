import numpy as np #import numpy library

#integers

i = 10 			#integer
print(type(i)) 	#print out the data type of i

a_i = np.zeros(i,dtype=int) #declare an array of ints
print(type(a_i))			#will return ndarray
print(type(a_i[0]))			#will return int64 (got int32 instead on Windows)

#floats

x = 119.0 #floating point number
print(type(x)) #print out the type of x

y = 1.19e2 #float 119 in scientific notation
print(type(y)) #print out the type of y

z = np.zeros(i,dtype=float)
print(type(z)) #print type of array
print(type(z[0])) #float

'''
This code prints out arrays from data types
'''
