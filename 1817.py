n, m = map(int, input().split())

def solve(n, m):
    if n == 0:
        return 0
    
    values = list(map(int, input().split()))

    cnt = 0
    tmpM=m
    for i in values:
        if tmpM - i>=0:
            tmpM-=i
            if tmpM==0:
                tmpM=m
                cnt+=1
        else:
            cnt+=1
            tmpM=m
            if tmpM - i>=0:
                tmpM-=i

    if m>tmpM>=0:
        cnt+=1
    return cnt

print(solve(n, m))