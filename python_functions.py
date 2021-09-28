import numpy as np
import sys

#define a fucntion that returns a value
def expo(x):
	return np.exp(x)	#return the np e^x fucntion

#define a subroutine that doeesn't return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i)))	#call the expo fucntion

#define a main function
def main():
	n = 10	#provide a default function for n

	#check it ther's a command line argument provided
	if(len(sys.argv)>1):
		n = int(sys.agrv[1])	#if an argument was provided, use it for n

	show_expo(n)		#call the show_expo subroutine

#run the main function
if__name__ == "__main__":
	main()