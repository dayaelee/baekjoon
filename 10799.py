# ()는 레이저다 

s = input()
stack=[]
cnt = 0
flag=0
for i in s:
    if i =='(':
        stack.append('(')
        flag=1
    elif i==')':
        if stack[-1] =='(':
            stack.pop()
            if stack and flag==1:
                if flag ==1:
                    cnt+=len(stack)
            if flag ==0:
                cnt+=1
            flag=0


    # print('난 ',i,'에요', stack, 'cnt: ', cnt)
print(cnt)