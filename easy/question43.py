#https://projecteuler.net/problem=43
#first, lets try brute force with few pruning strategy

raw = ['0','1','2','3','4','5','6','7','8','9']
candidate = []
def permute(list, index):
    for i in range(index, len(list)):
        list[index],list[i] = list[i],list[index]
        permute(list, index+1)
        list[index],list[i] = list[i],list[index]
    if index == len(list):
        if list[0] == '0':
            return
        elif list[5] != '5' and list[5] != '0':
            return
        else:
            temp = ''
            for j in range(len(list)):
                temp += list[j]
            candidate.append(temp)
permute(raw,0)
result = 0
for i in candidate:
    if int(i[1:4])%2 != 0:
        continue
    if int(i[2:5])%3 != 0:
        continue
    if int(i[3:6])%5 != 0:
        continue
    if int(i[4:7])%7 != 0:
        continue
    if int(i[5:8])%11 != 0:
        continue
    if int(i[6:9])%13 != 0:
        continue
    if int(i[7:10])%17 != 0:
        continue
    result += int(i)
print(result)
