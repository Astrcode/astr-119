#python_exceptions let you deal with un expected results


try:
	print(a) #this'll throw an execption because a isn't defined
except:
	print("a is not defined!")

#there are specific errors

try:
	print(a)	#will throw an exception
except NameError:
	print("a is still not defined!")
except:
	print("Something else went wrong")

#this will break out program
print(a)