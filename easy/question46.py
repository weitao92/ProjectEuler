#https://projecteuler.net/problem=46
#try brute force first
import math

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n+1):
        if i*i > n:
            break
        if n%i == 0:
            return False
    return True

initial = 1
primes = []

while True:
    initial += 2
    if isPrime(initial):
        primes.append(initial)
    else:
        test = False
        for p in primes:
            temp = math.sqrt((initial-p)/2)%1
            if temp == 0:
                test = True
                break
        if test == False:
            print(initial)
            break