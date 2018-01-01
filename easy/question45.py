#https://projecteuler.net/problem=45
#lower bound is given, the relation is not hard to find, use brute force
import math
n = 285
while True:
    n += 1
    t = n*(n+1)/2
    k = (n / math.sqrt(3))//1
    k += 1
    p = k*(3*k-1)/2
    if t != p:
        continue
    m = (n//2) + 1
    h = m*(2*m-1)
    if t != h:
        continue
    print(t)
    break