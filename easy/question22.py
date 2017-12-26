#https://projecteuler.net/problem=22

fp = open("name.txt", "r")
list = sorted(fp.read().split(","))

result = 0
for i in range(len(list)):
    name = list[i]
    temp = 0
    for j in range(1,len(name)-1):
        c = name[j:j+1]
        temp += ord(c) - ord('A') + 1
    result += temp * (i+1)
print result



