#https://projecteuler.net/problem=67

#dp approach

list = [None]*100
for i in range(100):
    list[i] = map(int, raw_input().split())

dp = [None]*100
dp[99] = list[99]
for i in range(98,-1,-1):
    dp[i] = [None]*(i+1)
    for j in range(i+1):
        dp[i][j] = list[i][j] + max(dp[i+1][j], dp[i+1][j+1])
print dp[0][0]
