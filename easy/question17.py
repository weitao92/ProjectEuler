#https://projecteuler.net/problem=17
#very trivial question, reminds me of ICPC mid-atlantic 2015

dict={1:3,2:3,3:5,4:4,5:4,6:3,7:5,8:5,9:4,10:3,11:6,12:6,13:8,14:8,15:7,16:7,17:9,18:8,19:8,20:6,30:6,40:5,50:5,60:5,70:7
      ,80:6,90:6,100:7}

def count(n):
    current = 0
    if n // 100 != 0:
        current += dict[n // 100]
        current += 7
        r = n % 100
        if r == 0:
            return current
        else:
            current += 3
            if r in dict:
                current += dict[r]
            else:
                current += count(r)
            return current
    else:
        if n // 10 < 2:
            return dict[n]
        else:
            d = n // 10
            current += dict[d*10]
            r = n % 10
            if r != 0:
                current += dict[r]
            dict[n] = current
            return current

result = 11
for i in range(1,1000):
    result += count(i)
print result
