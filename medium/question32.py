#question32, should be easy to implement with brute force with the upper bound

def comply(a, b, m):
    bag = set()
    for i in range(1,10):
        bag.add(str(i))
    for i in range(len(str(a))):
        c = str(a)[i:i+1]
        if c in bag:
            bag.remove(c)
        else:
            return False
    for i in range(len(str(b))):
        c = str(b)[i:i+1]
        if c in bag:
            bag.remove(c)
        else:
            return False
    for i in range(len(str(m))):
        c = str(m)[i:i+1]
        if c in bag:
            bag.remove(c)
        else:
            return False
    return True

result = 0
bag = set()
for i in range(1,10000):
    for j in range(i,10000):
        k = i*j
        if len(str(k)) + len(str(i)) + len(str(j)) == 9:
            if comply(i,j,k):
                if k not in bag:
                    result += k
                    bag.add(k)
        elif len(str(k)) + len(str(i)) + len(str(j)) > 9:
            break;
print result