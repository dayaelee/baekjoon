n = int(input())
result = 1
for i in range(n, 1, -1):
    result*=i
#print(result)


cnt = 0

realR = str(result)
realR = realR[::-1]
#print(realR)

check = 0
if '0' in realR:
    for i in realR:
        if i == '0':
            cnt+=1
        else:
            check = 1
        
        if check == 1:
            break
print(cnt)