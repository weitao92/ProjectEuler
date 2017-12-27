#https://projecteuler.net/problem=48
#use mod along with brute force, it can be done without mod in python though

result = 0
mod = 10**10
for i in range(1,1001):
    result %= mod
    temp = 1
    for j in range(1,i+1):
        temp *= i
        temp %= mod
    result += temp
print result
