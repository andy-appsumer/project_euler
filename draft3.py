from math import sqrt

def factors(number):
	factor_list = [number]

	for i in range (1,number // 2 +1):
		if number % i == 0:
			factor_list.append(i)
	return(factor_list)

"""
def top_factor(number):
	return factors(number)[-1]
print (top_factor(50))
"""
def isPrime(number):
	if len(factors(number)) == 2:
		#print True
		return True
	else:
		#print False
		return False

def prime_factors(number):
	pf_list = []
	for i in factors(number):
		if isPrime(i):
			pf_list.append(i)
	return pf_list

print (sqrt(600851475143))
print (prime_factors(775147))

pr
