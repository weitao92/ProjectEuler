#https://projecteuler.net/problem=36
#there ain't much under one million, can generate all then check binary

def isPalin(n):
    left = 0
    right = len(n)-1
    while left <= right:
        if n[left:left+1] != n[right:right+1]:
            return False
        left += 1
        right -= 1
    return True

list = [1,2,3,4,5,6,7,8,9]
for i in range(1,10):
    list.append(i*11)
    for j in range(0,10):
        list.append(i*101 + j*10)
        list.append(i*1001 + j*110)
        for k in range(0,10):
            list.append(i*10001 + j*1010 + k*100)
            list.append(i*100001 + j*10010 + k*1100)

result = 0
for i in list:
    b = str(bin(i))
    b = b[2:len(b)]
    if isPalin(b):
        result += i
print(result)

