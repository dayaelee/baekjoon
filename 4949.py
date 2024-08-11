while 1:
    s = input()
    if len(s)==1 and s[-1]=='.':
        break

    if s[-1]!='.':
        while 1:
            plus = input()
            s+=plus
            if plus[-1]=='.':
                break

    stack=[]
    check = 0
    for i in s:
        if i=='(':
            stack.append('(')
        elif i=='[':
            stack.append('[')
        elif i==')':
            if stack:
                if stack[-1]=='(':
                    stack.pop()
                else:
                    print('no')
                    check =1
                    break
            else:
                print('no')
                check = 1
                break
        elif i == ']':
            if stack:
                if stack[-1]=='[':
                    stack.pop()
                else:
                    print('no')
                    check = 1
                    break
            else:
                print('no')
                check = 1
                break
    if check ==0:
        if stack:
            print('no')
        else:
            print('yes')
        
    