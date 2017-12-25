#https://projecteuler.net/problem=19
#trivial question, hard coding problem

first = set() #set for first of month
firstDay = 1
first.add(firstDay)
for year in range(1901,2000):
    for month in range(1,13):
        if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
            firstDay += 31
        elif month == 4 or month == 6 or month == 9 or month == 11:
            firstDay += 30
        else:
            if year%4 == 0:
                firstDay += 29
            else:
                firstDay += 28
        first.add(firstDay)
first.remove(firstDay)
result = 0
sunday = 7
while sunday < firstDay:
    if sunday in first:
        result += 1
    sunday += 7
print result


