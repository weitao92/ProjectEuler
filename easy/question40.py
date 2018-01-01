#https://projecteuler.net/problem=40
#shouldn't be too hard to implemented, it's easy to find the upper bound

c = ''
for i in range(1,185186):
    c += str(i)
result = 1
index = 1
while index < 1000000:
    index *= 10
    result *= int(c[index-1:index])
print(result)
