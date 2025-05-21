import sys
input = sys.stdin.readline

dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]

n=int(input())
students=[]
for i in range(n*n):
    students.append(list(map(int, input().split())))

mapp=[[0] * n  for _ in range(n)]

def findzero(student):
    able=[[0] * n  for _ in range(n)]
    studen=student[1:]

    maxx=0
    # 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
    for i in range(n):
        for j in range(n):
            for xx in range(4):
                y = i+dy[xx]
                x = j+dx[xx]

                if 0<=y<n and 0<=x<n: 
                    if mapp[y][x] in studen and mapp[i][j]==0:
                        able[i][j]+=1
            if mapp[i][j]==0:
                maxx=max(maxx, able[i][j])
    bask=[]
    for i in range(n):
        for j in range(n):
            if able[i][j]==maxx:
                bask.append((i, j))

    return bask

cnt=0

def findzero2(tmp):
    able=[[0] * n  for _ in range(n)]
    tmpp=[]
    for t in tmp:
        i, j = t
        for xx in range(4):
            y = i+dy[xx]
            x = j+dx[xx]

            if 0<=y<n and 0<=x<n: 
                if mapp[y][x]==0:
                    able[i][j]+=1
        tmpp.append((able[i][j], i, j))

    return tmpp

while 1:
    tmp = findzero(students[cnt]) # zero basket
    if len(tmp)>1:
        tmp2 = findzero2(tmp)
        if tmp2:
            tmp2.sort(key = lambda x: (-x[0], x[1], x[2]))
            for i in tmp2:
                _, y, x = i
                if mapp[y][x]==0:
                    mapp[y][x] = students[cnt][0]
                    break
    else:
        for i in tmp:
            y, x = i
            if mapp[y][x]==0:
                mapp[y][x] = students[cnt][0]
                break

    cnt+=1

    if cnt==n*n:
        break

sum=0
for i in range(n*n):
    target = students[i][0]
    friends = students[i][1:]
    for ii in range(n):
        for j in range(n):
            if mapp[ii][j]==target:
                cnt=0
                for k in range(4):
                    y = ii+dy[k]
                    x = j + dx[k]
                    
                    if 0<=y<n and 0<=x<n: 
                        if mapp[y][x] in friends:
                            cnt+=1
                if cnt ==1:
                    sum+=1
                elif cnt ==2:
                    sum+=10
                elif cnt ==3:
                    sum+=100
                elif cnt ==4:
                    sum+=1000
print(sum)