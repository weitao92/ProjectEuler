#https://projecteuler.net/problem=24
#honestly i think i am cheating by using python's build-in permutation
import math
from itertools import permutations

# Get all permutations of [1, 2, 3]
perm = permutations([0,1,2,3,4,5,6,7,8,9])

print list(perm)[999999]

#here is my real solution

queue = [0,1,2,3,4,5,6,7,8,9]
result = [None]*10
limit = 999999
current = 9
fac = math.factorial(10)
for i in range(1,11):
    fac = fac/(current+1)
    temp = queue[limit // fac]
    result[i-1] = temp
    queue.remove(temp)
    limit %= fac
    current -= 1
print result

