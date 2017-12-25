# https://projecteuler.net/problem=15
import math

list = map(int, raw_input().split())
bigger = 0
smaller = 0
if list[0] >= list[1]:
    bigger = list[0]
    smaller = list[1]
else:
    bigger = list[1]
    smaller = list[1]
result = 1
for i in range(list[0]+list[1],bigger,-1):
    result *= i
print result / math.factorial(smaller)




