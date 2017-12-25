#https://projecteuler.net/problem=16
#implementation with BigInteger in Java is trivial, here is another solution:

list = [None]*500
list[0] = 2
current = 1
for i in range(2,1001):
    carry = 0
    index = 0
    while list[index] is not None:
        current = list[index]*2 + carry
        if current > 9:
            carry = 1
            list[index] = current%10
        else:
            carry = 0
            list[index] = current
        index += 1
    if carry != 0:
        list[index] = carry

sum = 0
index = 0
while list[index] is not None:
    sum += list[index]
    index += 1
print sum



