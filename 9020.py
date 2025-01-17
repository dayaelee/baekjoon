import sys
input = sys.stdin.readline

t = int(input())
visited = [False for i in range(10001)] # 0은 사용하지 않음
visited[0]=visited[1] = True # 소수가 아니면 True

print('hi;',int(10001**0.5) +1 )
for i in range(2, int(10001**0.5) +1 ): # 소수 판별기 
    if visited[i]==False:
        for j in range(i*i, 10001, i):
            visited[j]=True

def result(ele, n):
    left=0
    right=len(ele)-1
    total=[]
    while 1:
        if ele[left]+ele[right]==n:
            total.append([ele[left], ele[right]])
            right = len(ele)-1
            left+=1
            if left==len(ele):
                break
        else:
            right-=1
            if right==-1:
                left+=1
                right=len(ele)-1
                if left==len(ele):
                    break

    minN = float("inf")
    rA=0
    rB=0
    for i in total:
        a, b = i
        if minN>abs(a-b):
            rA=a
            rB=b
            minN=abs(a-b)
    tmp = [rA, rB]
    return sorted(tmp)
        
for i in range(t):
    n = int(input())
    ele=[]
    check = 0
    for j in range(1, n+1):
        if visited[j]==False:
            ele.append(j)
    if n%2==0:
        if n//2 in ele:
            check = 1
            print(str(n//2)+' '+str(n//2))
        else:
            resultTmp = result(ele, n)
    else:
        resultTmp = result(ele, n)

    if check == 0:
         print(' '.join(map(str, resultTmp)))