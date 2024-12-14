from collections import deque
import sys
input=sys.stdin.readline
n = int(input())

main=[]
main = deque(main)

for i in range(n):
    tmpString = input().strip()
    tmpString=tmpString.split(' ')
    #print(tmpString, 'tmpString')
    if len(tmpString)==1:
        if tmpString[0] == 'front':
            if len(main)!=0:
                print(main[0])
            else:
                print(-1)
        elif tmpString[0] == 'back':
            if len(main)!=0:
                print(main[-1])
            else:
                print(-1)
        elif tmpString[0] == 'size':
            print(len(main))
        elif tmpString[0] == 'empty':
            if len(main)!=0:
                print(0)
            else:
                print(1)
        elif tmpString[0] == 'pop':
            if len(main)!=0:
                print(main.popleft())
            else:
                print(-1)
    else:
        main.append(tmpString[1])

    #print(main)