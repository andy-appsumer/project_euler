

i=1
j = 1
threes = []
fives = []
while(3 * i < 1000):
	threes.append(3*i)
	i += 1
while(5 * j < 1000):
	fives.append(5*j)
	j += 1

both = threes + fives
both = list(set(both))
print sum(both)

