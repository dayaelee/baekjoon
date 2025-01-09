import sys 
input = sys.stdin.readline
n = int(input())
entire = []
for i in range(n):
    entire.append(list(map(int, input().split())))

packed=[0,0]

def recursion(startY, startX, target):
    color = entire[startY][startX]
    for i in range(startY, startY+target):
        for j in range(startX, startX+target):
            if color != entire[i][j]:
                newTarget = target//2
                recursion(startY, startX, newTarget) # one
                recursion(startY, startX + target//2, newTarget) #two
                recursion(startY + target//2, startX, newTarget) #three
                recursion(startY + target//2, startX + target//2, newTarget) #four
                return 

    if color == 0:
        packed[0]+=1
    else:
        packed[1]+=1


recursion(0,0, n)
print(packed[0])
print(packed[1])