t = int(input())

for i in range(t):
    s=input()
    stack=[]
    check =0
    for j in s:
        if j=='(':
            stack.append(0)
        else:
            if stack:
                stack.pop()
            else:
                print("NO")
                check=1
                break
    if check == 0:
        if stack:
            print("NO")
        else:
            print("YES")
    
    
    
