#https://projecteuler.net/problem=41
#just consider divisor 3 you will find n=7

def isPrime(n):
    if n <= 1:
        return False
    for i in range(2,n+1):
        if i*i > n:
            break
        if n%i == 0:
            return False
    return True

candidate = []
def permute(list, index):
    for i in range(index, len(list)):
        list[i],list[index] = list[index],list[i]
        permute(list,index+1)
        list[index], list[i] = list[i], list[index]

    if index == len(list)-1:
        c = ''
        for j in range(len(list)):
            c += list[j]
        candidate.append(int(c))
raw = ["1","2","3","4","5","6","7"]
permute(raw,0)
candidate.sort()

for i in range(len(candidate)-1,-1,-1):
    num = candidate[i]
    if isPrime(num):
        print(num)
        break

