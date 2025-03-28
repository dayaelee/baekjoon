import sys
input = sys.stdin.readline
import copy

dy=[1, -1, 0, 0]
dx=[0, 0, -1, 1]

def right(y, x, r, c):
    rem = newArr[y][c] # 맨 오른쪽 값 저장해놓고 up 호출할때 주기 
    tmp = newArr[y][2]
    for i in range(3, c+1):
        if i ==3:
            tmp = newArr[y][i-1]
        tmp2 = newArr[y][i]
        newArr[y][i]=tmp
        tmp = tmp2
    newArr[y][2]=0
    up(y, 1, r, c, rem)

def up(y, x, r, c, rem):
    newRem = newArr[1][c]
    # print('hi', rem, 'y', y, 'newRem', newRem)
    tmp = newArr[y-1][c]
    for i in range(y-1, 0, -1):
        if i == y-1:
            newArr[i][c]=rem
        else:
            tmp2 = newArr[i][c]
            newArr[i][c]=tmp
            # print('tmp:', tmp)
            tmp = tmp2
    left(y, 1, r, c, newRem)
    
def left(y, x, r, c, rem):
    # print('hi!!!', rem, 'y', y)
    newRem = newArr[1][1]
    tmp = newArr[1][c-1]
    for i in range(c-1, 0, -1):
        # print('i',i)
        if i == c-1:
            newArr[1][i]=rem
        else:
            tmp2 = newArr[1][i]
            newArr[1][i]=tmp
            tmp = tmp2
    # newRem = newArr[1][1]
    # print('???newRem', tmp)
    down(y, 1, r, c, tmp)
    
def down(y, x, r, c, rem): # 테스트 해봐야함 
    # print('hi~~', rem, 'y', y)
    # newRem = newArr[1][1]
    tmp = newArr[2][1]
    for i in range(2, y):
        if i == 2:
            newArr[i][1]=rem
        else:
            tmp2 = newArr[i][1]
            newArr[i][1]=tmp
            tmp = tmp2

def right2(y, x, r, c):
    rem = newArr[y][c] # 맨 오른쪽 값 저장해놓고 up 호출할때 주기 
    tmp = newArr[y][2]
    for i in range(3, c+1):
        if i ==3:
            tmp = newArr[y][i-1]
        tmp2 = newArr[y][i]
        newArr[y][i]=tmp
        tmp = tmp2
    newArr[y][2]=0
    down2(y, 1, r, c, rem)

def down2(y, x, r, c, rem):
    newRem = newArr[r][c]
    tmp = newArr[y+1][c]
    for i in range(y+1,r+1):
        if i == y+1:
            newArr[i][c]=rem
        else:
            tmp2=newArr[i][c]
            newArr[i][c] = tmp
            tmp = tmp2

    left2(y, 1, r, c, newRem)

def left2(y, x, r, c, rem):
    # print('hi', rem, 'y', y)
    newRem = newArr[r][1]
    tmp = newArr[r][c-1]
    for i in range(c-1, 0, -1):
        if i == c-1:
            newArr[r][i]=rem
        else:
            tmp2 = newArr[r][i]
            newArr[r][i]=tmp
            tmp = tmp2
    up2(y, 1, r, c, newRem)
    
def up2(y, x, r, c, rem):
    # print('hi?????', rem, 'y', y, "^^")
    tmp = newArr[r-1][1]
    for i in range(r-1, y, -1):
        if i == r-1:
            newArr[r-1][1] = rem
        else:
            tmp2 = newArr[i][1]
            newArr[i][1]=tmp
            tmp = tmp2

r, c, t = map(int, input().split())
arr=[[0]*(c+1)]

for i in range(r):
    arr.append([0]+list(map(int, input().split())))

time=1
while (1):

    newArr=[[0]*(c+1) for i in range(r+1)]

    # 공기청정기 찾기, 미세먼지 확산
    cleaning = -1 # 공청기의 꼬다리
    for i in range(1, r+1):
        for j in range(1, c+1):
            if arr[i][j]==-1:
                cleaning = i
                newArr[i][j] = -1
            
            if arr[i][j]>0:
                y=i
                x=j
                cnt=0
                for k in range(4):
                    ny=y+dy[k]
                    nx=x+dx[k]
                    if 1<=ny<r+1 and 1<=nx<c+1 and arr[ny][nx]!=-1:
                        cnt+=1
                        newArr[ny][nx]+=arr[y][x]//5
                arr[i][j]-=((arr[y][x]//5) * cnt)
                newArr[i][j] += arr[i][j]

    right(cleaning-1, 1, r, c)
    right2(cleaning, 1, r, c)

    # print()
    # for i in newArr:
    #     print(i)
    if time == t:
        break
    else:
        time+=1

    arr = copy.deepcopy(newArr)
    
# print()

# print('뭐지?')
summ = 0
for i in newArr:
    for j in i:
        if j>0:
            summ+=j
print(summ)
