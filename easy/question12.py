#https://projecteuler.net/problem=12

dict = {}
def numOfFactors(n):
    if n%2 == 0:
        n /= 2
    count = 0
    while n%2 == 0:
        count += 1
        n = n / 2
    count += 1

    divisor = 3
    while n != 1:
        temp = 0
        while n%divisor == 0:
            temp += 1
            n = n / divisor
        count *= (temp+1)
        divisor += 2
    return count

previous = 1
current = 1
triangle = 0
i = 3
while previous * current < 500:
    if triangle % 2 == 1:
        dict[triangle]=previous*current
    previous = current
    if i in dict:
        current = dict[i]
    else:
        current = numOfFactors(i)

    triangle = (i-1)*i / 2
    i += 1
print triangle

