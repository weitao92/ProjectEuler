#https://projecteuler.net/problem=20
#another trivial question

import math

text = str(math.factorial(100))
sum = 0
for i in range(len(text)):
    sum += int(text[i:i+1])
print sum