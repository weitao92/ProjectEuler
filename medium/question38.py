#https://projecteuler.net/problem=38

#by far the most interesting problem, they already provided a lower bound, so the number must starting with 9, that leave
#us with 8! candidate, talking about fixed number, it also must start with 9 with 4 digits only(analysis by cases)

candidate = []
def permute(list, index):
    for i in range(index, len(list)):
        list[i],list[index] = list[index],list[i]
        permute(list,index+1)
        list[index], list[i] = list[i], list[index]

    if index == len(list)-1:
        c = "9"
        for j in range(len(list)):
            c += list[j]
        candidate.append(int(c))
raw = ["1","2","3","4","5","6","7","8"]
permute(raw,0)
candidate.sort()

for i in range(len(candidate)-1,-1,-1):
    s = str(candidate[i])
    first = int(s[0:4])
    second = int(s[4:9])
    if first*2 == second:
        print(s)
        break

