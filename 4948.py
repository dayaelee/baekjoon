import sys
import math
input = sys.stdin.readline

all = [i for i in range(1, (123456*2)+1)]
checkall = [True for i in range(1, (123456*2)+2)]
for i in range(2, int(math.sqrt((123456*2)))+1):
    if checkall[i]==True:
        j = 2
        while i * j <= (123456*2)+1:
            if len(checkall)>i*j:
                checkall[i * j] = False
            j += 1

checkall[1]=False

def check(start, end):
    cnt = 0
    for i in range(start+1, end+1):
        if checkall[i] == True:
            cnt+=1
    return cnt

while 1:
    tmp = int(input())
    if tmp == 0:
        break
    doubleTmp = 2 * tmp
    result = check(tmp, doubleTmp)
    print(result)