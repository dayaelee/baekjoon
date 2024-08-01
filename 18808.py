import sys

n, m, k = map(int, sys.stdin.readline().split())

# 스티커 받고, 스티커 함에 넣기 
stickerPocket = []     # 모눈종이 각각 map 모음
stickerPocketEntire=[] # 모눈종이 r, l 모아놓는 함
for i in range(k):
    #모눈종이의 행, 열
    r, c = map(int, sys.stdin.readline().split()) 
    stickerPocketEntire.append([r,c])
    sticker=[]
    for j in range(r):
        tmp = list(map(int, sys.stdin.readline().split()))
        sticker.append(tmp)
    stickerPocket.append(sticker)

# 붙여졌나요?
visited=[[0] * m for i in range(n)]

# 90도 회전 함수
def rotation(cnt, i): 
    r, l = stickerPocketEntire[i] 
    # (90, 180, 270)도에 해당하게끔 3번만 돌림 
    
    sticker = stickerPocket[i]
    nn=len(sticker) # 기존의 행을 열로 사용
    mm=len(sticker[0]) # 기존의 열을 행으로 사용
    newSticker =[]

    for qq in range(mm):
        tmp=[]
        for pp in range(nn-1, -1, -1):
            tmp.append(sticker[pp][qq])
        newSticker.append(tmp)
    stickerPocket[i]=newSticker
    stickerPocketEntire[i]=[mm, nn]
    # 회전카운트 증가시킴
    cnt+=1  
    return cnt

def backtrack(p, q, i, visited):
    # 스티커를 붙일 수 없을 경우, 붙이려는 스티커를 붙이기 전 상태로 돌아오기위한것 
    rem = [item[:] for item in visited]
    # 붙이려는 스티커의 행열 조회
    r, c = stickerPocketEntire[i] 
    for j in range(r): # 행
        for jj in range(c): # 열
            #왼쪽 위부터 조회
            nr = p+j # 행/ 기존 행:n
            nc = q+jj # 열/ 기존 열:m
            # 스티커가 노트북 범위 안에 들어오면
            if 0<=nr<n and 0<=nc<m: 
                # 모눈종이에서 붙여야 하는 지점인 경우 
                if stickerPocket[i][j][jj]==1:
                    # 미리 붙여진 스티커가 없다.
                    if visited[nr][nc]!=1:
                        # 스티커 붙이기 
                        check = 1
                        visited[p+j][q+jj]=1
                    # 미리 붙여진 스티커가 있다. 겹친다.
                    else:
                        # 스티커를 붙이기 전(원래대로)으로 돌아가기 
                        visited=[item[:] for item in rem]
                        # 스티커를 못붙였다는 표식
                        check = 0
                        return visited, check
                # 모눈종이에서 빈칸인 경우
                else:
                    continue
            # 스티커가 노트북 범위 안에 못을어오면
            else:
                # 노트북 원상복구
                visited = [item[:] for item in rem]
                # 스티커를 못붙였다는 표식
                check = 0
                return visited, check
    # 스티커를 정상적으로 붙인 경우
    if check == 1:
        return visited, check

# 시작 스티커 번호
i=0
# 붙일 스티커 번호가 증가한 후 한번도 스티커를 회전한적 없는경우를 가리기 위한 변수
first=1
# 회전 횟수
cnt=0 
# 스티커를 붙이지 않았다는 표식
check=0
needRotation=0
while(1):
    rotat=0
    
    # 붙일 스티커가 없는 경우 종료 
    if i == k:
        break

    # 스티커의 행 열
    r, c = stickerPocketEntire[i]

    # 스티커의 행이나 열중 하나가 노트북을 벗어나는 경우
    if n<r or m<c: 
        #스티커의 행을 열로, 열을 행으로 바꿨을때(회전했을 때) 노트북에 들어가는 경우
        if c<=n and r<=m: 
            if cnt <3: # 0-0, 90-1, 180-2, 270-3
                cnt = rotation(cnt, i)
                rotat = 1
            # 회전을 4번다 한 경우, 다음 스티커로 넘어감 
            else:
                i+=1
                cnt=0
                first=1
        # 스티커의 행을 열로, 열을 행으로 바꿨을때(회전했을 때) 노트북에 안들어가는 경우=붙일 수 없는 경우
        elif c>n and r>m:
            # 다음 스티커로 넘어감 
            first=1
            i+=1
            cnt=0

    # 스티커가 붙여지지 않았고 0도 일때 스티커 붙이는 시도를 다 해본경우 
    # 회전이 270까지 되지 않은 경우=> 회전
    if check == 0 and first==0 and rotat==0 and needRotation==1:
        if cnt<=3:
            cnt = rotation(cnt, i)
        
    for p in range(n):
        for q in range(m):
            # 한번 돌았으면 first=0
            rotat=0
            first=0
            
            # 붙일 스티커가 없는 경우 종료 
            if i == k:
                break

            # 붙일 스티커 붙여보기 
            visited, check = backtrack(p, q, i, visited)
            #스티커를 제대로 붙였으면 빠져나감
            if check==1: 
                break
        #다음으로 붙일 스티커로 넘어가고, 회전 횟수 초기화
        #스티커를 붙였으면 빠져나감
        if check==1:
            check = 0
            i+=1
            cnt=0
            first=1
            needRotation=0
            break
    if check == 0:
        needRotation=1

    if cnt==3:
        i+=1
        first=1
        cnt=0

    # 붙일 스티커가 없는 경우 종료 
    if i ==k:
        break

# 노트북에 붙여진 스티커 개수 세기
sum=0
for end in visited:
    for end2 in end:
        if end2==1:
            sum+=1
print(sum)