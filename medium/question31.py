coins = [1,2,5,10,20,50,100,200]
coins.reverse()
print coins
def cal(n, index):
    if n == 0:
        return 1
    if n < 0:
        return 0
    if index == len(coins)-1:
        return 1
    result = 0
    coin = coins[index]
    while n >= 0:
        result += cal(n, index+1)
        n -= coin
    return result
print cal(200,0)