#https://projecteuler.net/problem=23

def count(n):
    sum = 1
    for i in range(2,n):
        if n / i < i:
            break
        if n%i == 0:
            sum += i
            if n/i != i:
                sum += n/i
    return sum
list = []
for i in range(1,28124):
    if count(i) > i:
        list.append(i)
bag = set()
for i in range(1,28124):
    bag.add(i)

for i in range(len(list)):
    for j in range(i,len(list)):
        bag.discard(list[i]+list[j])
result = sum(bag)
print result
