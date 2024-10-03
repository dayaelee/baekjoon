

n = int(input())

mapp= [0 for _ in range(n)]
cnt=[0]

def chess(depth, cnt):
    if depth == n:
        cnt[0]+=1
        return 
    
    for i in range(n):
        mapp[depth] = i

        if possible(depth):
            chess(depth+1, cnt)

def possible(col):
    for i in range(col):
        # 같은 열에 있는지 
        if mapp[i] == mapp[col]: # depth 추가하기전 
            return False
    
        # 대각선에 있는지 
        if abs(mapp[i]-mapp[col]) == abs(i-col):
            return False
    return True


chess(0, cnt)
print(cnt[0])