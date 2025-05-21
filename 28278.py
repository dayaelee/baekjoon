import sys
input = sys.stdin.readline

n=int(input())
stack=[]
for i in range(n):
    o= list(input().split())
    if o[0]=='1':
        stack.append(o[1])
    elif o[0]=='2':
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif o[0]=='3':
        print(len(stack))
    elif o[0]=='4':
        if stack:
            print(0)
        else:
            print(1)
    elif o[0]=='5':
        if stack:
            print(stack[-1])
        else:
            print(-1)

