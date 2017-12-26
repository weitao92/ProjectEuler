#https://projecteuler.net/problem=21
#brute-force-solution
import math

def sum(n):
    sum = 1
    for i in range(2,n):
        if n / i < i:
            break
        if n%i == 0:
            sum += i
            if n/i != i:
                sum += n/i
    return sum
list = [sum(i) for i in range(1, 10000)]
list[0] = 0

checked = [False]*9999
result = 0
for i in range(9999):
    if list[i] >= 10000 or checked[i]:
        continue
    if list[list[i]-1] == i+1 and list[i] != i+1:
        result += (i+1+list[i])
        checked[list[i]-1] = True
print result


