#https://projecteuler.net/problem=50
#generate one prime list, one prime set and a cumulated sum list

def primes(n):
	if n==2: return [2]
	elif n<2: return []
	s=range(3,n+1,2)
	mroot = n ** 0.5
	half=(n+1)/2-1
	i=0
	m=3
	while m <= mroot:
		if s[i]:
			j=(m*m-3)/2
			s[j]=0
			while j<half:
				s[j]=0
				j+=m
		i=i+1
		m=2*i+3
	return [2]+[x for x in s if x]

limit = 1000000
list = primes(limit)
sums = [None]*len(list)
sums[0] = list[0]
bag = set()
bag.add(2)
for i in range(1,len(list)):
    sums[i] = sums[i-1] + list[i]
    bag.add(list[i])
length = 21

result = 0
outer = True
for i in range(21,len(list)):
    if outer == False:
        break
    for j in range(i-length,-1,-1):
        diff = sums[i]-sums[j]
        if diff >= limit:
            outer = False
            break
        if diff in bag:
            result = diff
            length = i-j+1
print(str(result) + " " + str(length))




