import sys
input = sys.stdin.readline

n = int(input())

tmp = list(map(int, input().split()))
b, c = map(int, input().split())

# b = 총감독관 감시자. c = 부감독관 감시자 
total = 0
for i in tmp:
    value = i 
    value -=b
    total+=1
    if value > 0:
        total+=(value // c)
        if value % c>0:
            total+=1
print(total)

