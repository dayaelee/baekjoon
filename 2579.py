import sys
import itertools

input = sys.stdin.readline

n = int(input())

stair=[0,]

for i in range(n):
    stair.append(int(input()))


check=[[0,0,0], [0,stair[1], stair[1]],]

for i in range(2, n+1):
    checkTmp = []
    checkTmp.append(max(check[i-1][1], check[i-1][2]))
    checkTmp.append(check[i-1][0]+stair[i])
    checkTmp.append(check[i-1][1]+stair[i])
    check.append(checkTmp)

print(max(check[n][1], check[n][2]))

