#first, let's try brute force

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n+1):
        if i*i > n:
            break
        if n%i == 0:
            return False
    return True

def isEven(n):
    if n == 0:
        return False
    return n%2 == 0

def isCircular(n, bag):
    removed = set()
    removed.add(n)
    text = str(n)
    if len(text) == 1:
        bag.remove(n)
        return 1
    for i in range(1,len(text)):
        changed = text[i:len(text)] + text[0:i]
        removed.add(int(changed))
        if int(changed) not in bag:
            return 0
    for i in removed:
        bag.remove(i)
    return len(removed)



bag = set()
bag.add(2)
i = 3
step = 10
while i < 1000000:
    if isEven(i//100000):
        i += 100000
    if isEven(i//10000):
        i += 10000
    if isEven(i//1000):
        i += 1000
    if isEven(i//100):
        i += 100
    if isEven(i//10):
        i += 10
    if isPrime(i):
        bag.add(i)

    i += 2
print len(bag)
num = 0
bag1 = set()
for i in bag:
    bag1.add(i)
for i in bag:
    if i in bag1:
        f = isCircular(i,bag1)
        if f != 0:
            num += f
print num


