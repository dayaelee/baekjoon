box=0
result=0
for i in range(4):
    o, i = map(int, input().split())
    box-=o
    box+=i
    result=max(box, result)

print(result)