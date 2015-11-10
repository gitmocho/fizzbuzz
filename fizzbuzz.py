"""
Write a program 
-  prints the numbers from 1 to 100. 
- But for multiples of three print 'Fizz' instead of the number 
- and for the multiples of five print Buzz. 
- numbers which are multiples of both three and five print FizzBuzz. Sample output:

"""
x = 0
for x in range(0,100):	
	if x % 3 == 0 and x % 5 == 0:
		print ('Fizz Buzz')	
	elif x % 3 == 0:  	
		print ('Fizz') 
	elif x % 5 == 0:
		print ('Buzz')
	else:
		print (x)

x = x + 1
