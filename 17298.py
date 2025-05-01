n = int(input())
a = list(map(int, input().split()))

stack=[]
ans=[-1] * n

for i in range(len(a)):
    v = a[i]
    while stack and a[stack[-1]]<v:
        idx = stack.pop()
        ans[idx]=v
    else:
        stack.append(i)

print(' '.join(map(str, ans)))