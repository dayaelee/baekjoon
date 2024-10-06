day = int(input())

car  = list(map(int, input().split()))
cnt = 0
for i in car:
    if i == day:
        cnt+=1
print(cnt)