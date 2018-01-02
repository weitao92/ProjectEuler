#https://projecteuler.net/problem=53
#if the partition is too separated then the combinations will be small.
import math
limit = 1000000
result = 4

for n in range(24,101):
    bound = n//2
    current = 1
    m = n
    for temp in range(1,bound+1):
        current *= m
        current /= temp
        m -= 1
        if current > limit:
            if n%2 == 1:
                result += (bound - temp + 1)*2
            else:
                result += (bound - temp + 1)*2 - 1
            break
print(result)
