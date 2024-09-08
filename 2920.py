tmp = list(map(int, input().split()))

cnt1 = 1
check1 = 0
for i in range(0, len(tmp)):
    if cnt1==tmp[i]:
        check1=1
    else:
        check1=0
        break
    cnt1+=1


cnt2 = 8
check2 = 0
for i in range(0, len(tmp)):
    if cnt2==tmp[i]:
        check2=1
    else:
        check2=0
        break
    cnt2-=1



if check1==1:
    print('ascending')

if check2==1:
    print('descending')

if check1 ==0 and check2 ==0:
    print('mixed')
