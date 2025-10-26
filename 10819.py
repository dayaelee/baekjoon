n = int(input())
a = list(map(int, input().split()))

def detail(a, b):
    return abs(a-b)

answer = 0

def cal(target): # a[n-1], a[n]
    tmpAnswer=0

    for i in range(len(target)-1):
        tmpAnswer+=detail(target[i], target[i+1])
    return tmpAnswer
    
visited=[False for _ in range(len(a))]
tmp = []

def backtrack(tmpList, cnt):
    global answer
    if cnt == len(a):
        # print(tmpList)
        answer = max(answer, cal(tmpList))
        return 
    
    for i in range(len(a)):
        if visited[i]==False:
            tmpList.append(a[i])
            visited[i]=True
            backtrack(tmpList, cnt+1)
            tmpList.pop()
            visited[i]=False

backtrack(tmp, 0)
print(answer)


