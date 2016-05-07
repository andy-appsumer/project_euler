"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

def sum_3s_and_5s(number):
	n = number
	sum = 0
	for i in range (0, n):
		if i % 3 == 0 or i % 5 == 0:
			sum += i

	return (sum)

print( "First test when n = 10")
x = sum_3s_and_5s(10)
print("sum = " + str(x))

print( "Next Find sum for n = 1000")
y = sum_3s_and_5s(1000)
print("sum = " + str(y))



