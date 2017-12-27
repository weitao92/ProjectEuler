#https://projecteuler.net/problem=26
#design a simple hash function and use map to find the cycle

def countCycle(n):
    map = {}
    current = 1
    index = 0
    while True:
        current *= 10
        temp = current / n
        hash = current * 1000 + temp
        if hash in map:
            return index - map[hash]
        map[hash] = index
        current = current % n
        index += 1
    return index
max = 0
result = 0
for i in range(1,1000):
    current = countCycle(i)
    if current > max:
        max = current
        result = i
print result


