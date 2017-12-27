#https://projecteuler.net/problem=25

list = [1,1]
index = 2
while True:
    temp = list[index-2] + list[index-1]
    list.append(temp)
    index += 1
    if len(str(temp)) >= 1000:
        break
print index
