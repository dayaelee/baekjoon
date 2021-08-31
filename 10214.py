n = int(input())
if n == 0:
    quit()
ysum=0
ksum=0
for i in range(n):
    for i in range(9):
        a = input().split()
        ysum += int(a[0])
        ksum += int(a[1])

    if ysum > ksum:
        print('Yonsei')
    elif ysum < ksum:
        print('Korea')
    else:
        print('Draw')
