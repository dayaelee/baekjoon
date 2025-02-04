import sys
input = sys.stdin.readline

n = int(input())
time=[]
for i in range(n):
    time.append(list(map(int, input().split())))
time.sort(key = lambda x: (x[1], x[0]))

i = 0
j = 1
cnt = 1
while j<n:
    if time[i][1]<= time[j][0]:
            cnt+=1
            i=j
            j+=1
    else:
        j+=1
print(cnt)