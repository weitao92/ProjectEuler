#https://projecteuler.net/problem=42
#easy implementation problem
import math
fp = open("names.txt")
text = fp.read()
list = text.split(",")
list = map(lambda x: x[1:len(x)-1], list)

result = 0
for s in list:
    value = 0
    for i in range(len(s)):
        value += ord(s[i:i+1]) - ord('A') + 1
    value *= 2
    n = math.sqrt(value)//1
    next = n+1
    if n*next == value:
        result += 1
print(result)

