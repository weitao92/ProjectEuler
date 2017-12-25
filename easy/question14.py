#https://projecteuler.net/problem=14

dict = {1:1}
max = 0
result = 0
for i in range(2,1000000):
    length = 0
    origin = i
    while origin != 1:
        if origin in dict:
            origin = dict[origin]
        else:
            next = 0
            if origin%2 == 0:
                next = origin/2
            else:
                next = 3*origin + 1
            dict[origin] = next
            origin = next
        length += 1
    if length > max:
        max = length
        result = i

print result
print max
