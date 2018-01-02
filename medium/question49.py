#https://projecteuler.net/problem=49
#implementation problem

def same(a, b):
    bag1 = set()
    bag2 = set()
    for i in range(0,len(a)):
        c = a[i:i+1]
        bag1.add(c)
    for i in range(0,len(b)):
        c = b[i:i+1]
        bag2.add(c)
    if len(bag1) != len(bag2):
        return False

    for i in range(0,len(a)):
        c = a[i:i+1]
        if c not in bag2:
            return False
    return True

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

list = primes(10000)
list = filter(lambda x: len(str(x)) == 4, list)
bag = set(list)
finished = False
for i in range(0,len(list)):
    if finished == True:
        break
    current = list[i]
    if current == 1487:
        continue
    for j in range(i+1,len(list)):
        next = list[j]
        if same(str(current), str(next)):
            third = 2*next-current
            if third in bag:
                if same(str(current), str(third)):
                    print(str(current)+str(next)+str(third))
                    finished = True
                    break
