#another implementation problem, after finding the upper bound should be easy to solve

def fac(n):
    if n == 0:
        return 1
    result = n
    while n > 1:
        n -= 1
        result *= n
    return result

c = fac(9)
temp1 = c
temp2 = 9

while temp1 > temp2:
    temp1 += c
    temp2 *= 10
    temp2 += 9
result = 0
for i in range(3,temp2):
    sum = 0
    for j in range(0,len(str(i))):
        n = int(str(i)[j:j+1])
        sum += fac(n)
    if sum == i:
        print i
        result += i
print result
