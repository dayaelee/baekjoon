# 괄호열이 뭔지? 

# 올바른 괄호열인지 체크 = 쌍을 이루는지 체크

# 닫기를 시작했을때, 계산시작 
# () = 2, [] = 3

# 다 닫고(if stack:) 새로 열때 +

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
        print('좋다  시작하자 ')
        # checkingStack = []
        # cal=''
        # for j in s:
        #     if j=='(':
        #         if not checkingStack:
        #             cal+='(+2'
        #             checkingStack.append(j)
        #         else:
        #             if checkingStack[-1]=='(':
        #                 cal+='*((2'
        #                 checkingStack.append(j)
        #             elif checkingStack[-1]=='[':
        #                 cal+='(2'
        #                 checkingStack.append(j)
        #             elif checkingStack[-1]==')' or checkingStack[-1]==']':
        #                 cal+='+(2'
        #                 checkingStack.append(j)
        #     elif j=='[':
        #         if not checkingStack:
        #             cal+='(+3'
        #             checkingStack.append(j)
        #         else:
        #             if checkingStack[-1]=='[':
        #                 cal+='*3'
        #                 checkingStack.append(j)
        #             elif checkingStack[-1]=='(':
        #                 cal+='(3'
        #                 checkingStack.append(j)
        #             elif checkingStack[-1]==']' or checkingStack[-1]==')':
        #                 cal+='+(3'
        #                 checkingStack.append(j)

        #     elif j==')':
        #         if checkingStack[-1]=='(':
        #             cal+=')'
        #             checkingStack.pop()
        #     elif j==']':
        #         if checkingStack[-1]=='[':
        #             cal+=')'
        #             checkingStack.pop()

        #     print('')
        #     print('j: ', j)
        #     print(checkingStack)
        #     print('cal',cal)
        check = 0

        # + 추가 작업 // replace, find 다시 공부하기 
        while 1:
            check = 0

            result1 = s.find(")(")
            result2 = s.find("][")
            result3 = s.find(")[")
            result4 = s.find("](")

            if result1!=-1:
                s=s.replace(")(", ")+(")
                check =1
            elif result2!=-1:
                s=s.replace("][", "]+[")
                check =1
            elif result3!=-1:
                s=s.replace(")[", ")+[")
                check =1
            elif result4!=-1:
                s=s.replace("](", "]+(")
                check =1

            if check == 0:
                break
        print('result:', s)
        
        # 2, 3 교체 작업 

        while 1:
            check = 0
            result1 = s.find("()")
            result2 = s.find("[]")

            if result1!=-1:
                s=s.replace("()", "2")
                check =1
            elif result2!=-1:
                s=s.replace("[]", "3")
                check =1
            
            if check == 0:
                break

        print('result?:', s)





            




