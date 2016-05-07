def sum(list):
	total = 0
	for l in list:
		total += l
	return total

def fibonacci(number):
	f_list = [1,2]
	n = number
	for j in range(2,n):
		jth_term = f_list[j-2] + f_list[j-1]
		f_list.append(jth_term)
	return f_list
	
print(fibonacci(10))
