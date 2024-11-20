

n, m = map(int, input().split())

# 길이가 m인 수열을 모두 구하는 프로그램

# 1부터 자연수 N까지 중복 없이 M개를 고른 수열

result=[]
cnt =0

def backtrack(cnt, now, result):

    for j in range(now, n+1):
        result.append(j)
        cnt+=1
        if len(result)<m:
            backtrack(cnt, j+1, result)
            result.pop()
        elif len(result)==m:
            print(" ".join(map(str, result)))
            result.pop()

for i in range(1, n+1):
    result.append(i)
    cnt+=1
    if len(result)==m:
        print(" ".join(map(str, result)))
    else:
        backtrack(cnt, i+1, result)
    result.pop()
