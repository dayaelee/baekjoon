import sys
input = sys.stdin.readline

n = int(input())
total = [list(map(int, input().split())) for i in range(n)]

Alltotal=[0,0,0]

def valid(startY, startX, size):
    value = total[startY][startX]
    for i in range(startY, startY + size):
        for j in range(startX, startX + size):
            if total[i][j] != value:
                return False
    return True

def magic(startY, startX, n):
    if valid(startY, startX, n):
        Alltotal[total[startY][startX]+1] +=1
        return 
    
    next = n // 3
    for i in range(3):
        for j in range(3):
            magic(startY+(next*i), startX + (next*j), next)

Alltotal=[0, 0, 0]
magic(0, 0, n)

for i in Alltotal:
    print(i)