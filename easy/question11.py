n = 20
matrix = [[0 for i in range(n)] for j in range(n)]
for i in range(n):
    matrix[i] = list(map(int, raw_input().split()))

max = -1;
for i in range(n):
    for j in range(n):
        if i >= 3:
            product = matrix[i][j]*matrix[i-1][j]*matrix[i-2][j]*matrix[i-3][j]
            if product > max:
                max = product
        if i <= 16:
            product = matrix[i][j]*matrix[i+1][j]*matrix[i+2][j]*matrix[i+3][j]
            if product > max:
                max = product
        if j >= 3:
            product = matrix[i][j] * matrix[i][j-1] * matrix[i][j-2] * matrix[i][j-3]
            if product > max:
                max = product
        if j <= 16:
            product = matrix[i][j] * matrix[i][j+1] * matrix[i][j+2] * matrix[i][j+3]
            if product > max:
                max = product

        if i >= 3 and j >= 3:
            product = matrix[i][j]*matrix[i-1][j-1]*matrix[i-2][j-2]*matrix[i-3][j-3]
            if product > max:
                max = product
        if i <= 16 and j >= 3:
            product = matrix[i][j]*matrix[i+1][j-1]*matrix[i+2][j-2]*matrix[i+3][j-3]
            if product > max:
                max = product
        if i >= 3 and j <= 16:
            product = matrix[i][j]*matrix[i-1][j+1]*matrix[i-2][j+2]*matrix[i-3][j+3]
            if product > max:
                max = product
        if i <= 16 and j <= 16:
            product = matrix[i][j]*matrix[i+1][j+1]*matrix[i+2][j+2]*matrix[i+3][j+3]
            if product > max:
                max = product

print max


