s = input()
stack=[]
check = 0
for i in s:
    if i =='(':
        stack.append('(')
    elif i == '[':
        stack.append('[')
    elif i == ')':
        if stack:
            if stack[-1]=='(':
                stack.pop()
            else:
                check = 1
                print(0)
                break
        else:
            check = 1
            print(0)
            break
    elif i == ']':
        if stack:
            if stack[-1]=='[':
                stack.pop()
            else:
                check = 1
                print(0)
                break
        else:
            check =1
            print(0)
            break
if check == 0:
    if stack:
        print(0)
    else:
        checkingStack = []
        result=0
        tmpV=1
        for index, j in enumerate(s):
            if j=='(':
                tmpV*=2
                check =1
                checkingStack.append('(')
            elif j=='[':
                tmpV*=3
                check =1
                checkingStack.append('[')

            elif j==')':
                if check ==1: # 최초로 닫는괄호 
                    result+=tmpV
                    tmpV=tmpV//2
                    check=0
                    checkingStack.pop()
                else:
                    tmpV=tmpV//2
                    checkingStack.pop()

            elif j==']':
                if check ==1: # 최초로 닫는괄호 
                    result+=tmpV
                    tmpV=tmpV//3
                    check=0
                    checkingStack.pop()
                else:
                    tmpV=tmpV//3
                    checkingStack.pop()

            #print('checkingStack', checkingStack, ' result: ', result, 'index: ', index, ' tmpV: ', tmpV)
        print(result)