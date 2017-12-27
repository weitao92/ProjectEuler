#https://projecteuler.net/problem=29
#first try brute-force with set, trying to figure out a better way by factorization

bag = set()
for i in range(2,101):
    for j in range(2,101):
        bag.add(i**j)
print len(bag)