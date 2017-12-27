#https://projecteuler.net/problem=28
#i think there will be a smarter way but let's try simulation first, second solution is below

mat = [[0 for x in range(1001)] for y in range(1001)]
row = 0
col = 1000
current = 1001 * 1001
face = 3
for i in range(1001*1001):
    mat[row][col] = current
    current -= 1
    if face == 0:
        if row - 1 < 0 or mat[row-1][col] != 0:
            face = 3
            col -= 1
        else:
            row -= 1
    elif face == 1:
        if col + 1 > 1000 or mat[row][col+1] != 0:
            face = 0
            row -= 1
        else:
            col += 1
    elif face == 2:
        if row + 1 > 1000 or mat[row+1][col] != 0:
            face = 1
            col += 1
        else:
            row += 1
    else:
        if col - 1 < 0 or mat[row][col-1] != 0:
            face = 2
            row += 1
        else:
            col -= 1

result = 0
for i in range(1001):
    result += mat[i][i]
    result += mat[i][1000-i]
result -= mat[500][500]
print result

#Here is the second way using cornors
result = 0
for i in range(1001,1,-2):
    result += 4*(i**2) - 6*i + 6
result += 1
print result
