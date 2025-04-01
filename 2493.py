n = int(input())
building = list(map(int, input().split()))

answer = [0] * len(building)
stack = []

for i in range(len(building)-1, -1, -1):
    if i == len(building)-1:
        stack.append([building[i], i])
    else:
        if stack:
            if stack[-1][0] < building[i]:
                while 1:
                    if stack:
                        if stack[-1][0] < building[i]:
                            indexx=stack[-1][1]
                            answer[indexx]=i+1
                            stack.pop()
                        else:
                            break
                    else:
                        break
                stack.append([building[i], i])
            else:
                stack.append([building[i], i])
print(' '.join(map(str,answer)))
            
