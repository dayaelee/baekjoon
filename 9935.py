s = input()
tnt = input()
stack=[]
for i in s:
    stack.append(i)
    if len(stack)>=len(tnt) and ''.join(stack[-len(tnt):])==tnt:
        # stack=stack[:-len(tnt)]
        del stack[-len(tnt):]
if stack:
    print(''.join(stack))
else:
    print('FRULA')