#https://projecteuler.net/problem=30
#first try to find the upper bound then try brute force

c = 9**5
current = c
base = 9
while current > base:
    current += c
    base = base * 10 + 9

result = 0
for i in range(2,base):
    temp = 0
    for j in range(len(str(i))):
        temp += int(str(i)[j:j+1])**5
    if temp == i:
        print temp
        result += temp
print result