import math
a, p = map(int, input().split())

ll = [a]

tmp = list(str(a))
# cnt = 0
rem = -1
while 1:
    sum = 0
    for i in range(len(tmp)):
        
        sum += int(math.pow(int(tmp[i]), p))
    if sum not in ll:
        ll.append(sum)
        tmp = list(str(sum))
        # cnt+=1
    else:
        rem = sum
        break

# print(ll)
# print(rem)

for i in range(len(ll)):
    if ll[i]==rem:
        print(i)
        # print(cnt)
        break


