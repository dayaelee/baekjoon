n = int(input())
time =[]
for i in range(n):
    time.append(list(map(int, input().split())))

print(time)

time.sort(key = lambda x: (-x[1]))

print(time)
answer =-1


answer = time[0][1]

print('^^', answer)
cnt = 0

while cnt<len(time):
    if answer <= time[cnt][1]:
        answer -= time[cnt][0]
        cnt+=1
    else:
        answer-=1

    print('answer, cnt', answer, cnt)
if answer <0:
    print(-1)
else:
    print(answer)