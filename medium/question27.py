#https://projecteuler.net/problem=27

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n+1):
        if i*i > n:
            break
        if n%i == 0:
            return False
    return True

def length(a,b):
    n = 0
    current = b
    result = 0
    if isPrime(current):
        result = 1
    else:
        return 0
    while True:
        n += 1
        current = n**2 + a*n + b
        if(isPrime(current)):
            result += 1
        else:
            break
    return result

max = 0
a = 0
b = 0
for i in range(-999,1000):
    for j in range(-1000,1001):
        temp = length(i,j)
        if temp > max:
            max = temp
            a = i
            b = j
print a*b