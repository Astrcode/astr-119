import numpy as np		#we use numpy for lots of things

def main():
	i = 0             	#integers can be delcared with a number
	n = 10              #another integer  
	x = 119.0           #floating point nums are declared with a "."


	y = np.zeros(n,dtype=float)

	# we can use for loops to declare arrays quickly

	for i in range(n):             #i in range [0,n-1]
		y[i] = 2.0 * float(i) + 1. #set y = 2i+1 as floats

	# we can also simply iterate through a variable
	for y_element in y:
		print(y_element)

#execute the main function
if __name__ == "__main__":
	main()
