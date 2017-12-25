#https://projecteuler.net/problem=18

#dp approach

list = [None]*15
for i in range(15):
    list[i] = map(int, raw_input().split())

dp = [None]*15
dp[14] = list[14]
for i in range(13,-1,-1):
    dp[i] = [None]*(i+1)
    for j in range(i+1):
        dp[i][j] = list[i][j] + max(dp[i+1][j], dp[i+1][j+1])
print dp[0][0]
