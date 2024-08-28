import sys
n = int(input())

input = sys.stdin.readline

for i in range(n):
    tmpS=input().strip()
    if len(tmpS)>=6 and len(tmpS)<=9:
        print('yes')
    else:
        print('no')