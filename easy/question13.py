#https://projecteuler.net/problem=13

sum = 0
for i in range(100):
    temp = int(raw_input())
    sum += temp

print str(sum)[:10]