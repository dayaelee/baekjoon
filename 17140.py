import sys
from collections import defaultdict
input = sys.stdin.readline

rr, cc, k = map(int, input().split())
a=[]
for i in range(3):
    a.append(list(map(int, input().split())))

def rcCheck(target):
    r = len(target)
    c = len(target[0])
    return r, c

def operation(target, type):
    maxL = 0
    if type ==1:
        for i in range(len(target)): # 행 순회 
            dict=defaultdict(int)
            for j in target[i]: # 각각의 수가 몇번 나왔는지 체크 
                dict[j]+=1 
            dict = sorted(dict.items(), key = lambda x: (x[1], x[0]) ) # 등장수 기준 오름차순 
            n=[]
            for key, value in dict: # 갱신 
                if key == 0: # 0은 무시 
                    continue
                n.append(key)
                n.append(value)
                if len(n)>=100: # 원소 개수 100을 넘어가면 이하는 버림 
                    maxL=100
                    n=n[:100]
                    break
            
            maxL=max(len(n), maxL) # 가장 큰 행의 길이
            target[i]=n
        
        for i in range(len(target)): # 가장 큰 행의 길이만큼 0 채우기 
            while len(target[i])<maxL:
                target[i].append(0)

        return target
    else: # 행에 있는 수 정렬
        box =[]
        for j in range(len(target[0])):
            dict=defaultdict(int)
            for i in range(len(target)):
                key=target[i][j]
                dict[key]+=1
            dict = sorted(dict.items(), key = lambda x: (x[1], x[0]) ) # 등장수 기준 오름차순 
            n=[]
            for key, value in dict: # 갱신 
                if key == 0: # 0은 무시 
                    continue
                n.append(key)
                n.append(value)
                if len(n)>=100: # 원소 개수 100을 넘어가면 이하는 버림 
                    maxL=100
                    n=n[:100]
                    break
            maxL=max(len(n), maxL) # 가장 큰 행의 길이
            box.append(n)
        new = [ [0]*len(box) for _ in range(maxL)]
        for i in range(len(box)):
            for j in range(len(box[i])):
                new[j][i]=box[i][j]
        return new 
    
cnt = 0
while 1:
    if len(a)>rr-1 and len(a[0])>cc-1:
        if a[rr-1][cc-1]==k:
            print(cnt)
            break

    if cnt>=101:
        print(-1)
        break

    r, c = rcCheck(a)
    flag = 0
    if r >= c :
        flag = 1 # 행 정렬
    else:
        flag = 0 # 열 정렬

    a=operation(a, flag)
    cnt+=1