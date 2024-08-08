n = int(input())
cnt=0
for i in range(n):
    s = input()
    stack=[]
    check = 0
    for index, j in enumerate(s):
        if stack:
            if stack[-1] == j:
                stack.pop()
            else:
                stack.append(j)
        else:
            stack.append(j)

    if not stack:
        cnt+=1
        # print('cnt', cnt)
print(cnt)