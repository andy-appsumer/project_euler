"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""
"""
def isPrime(number):
	prime = True
	for i in range (2, number):
		if number % i == 0:
			prime = False
			break
	return prime

x = 775147
primes = []

for i in range(2, x +1):
	if isPrime(i) == True:
		primes.append(i)

print(primes)
"""
n = 600851475143
i = 2
while i * i < n:

     while n % i == 0:
         n = n / i
     print "i = " + str(i) + " : n = " + str(n)
     i = i + 1

print (n)