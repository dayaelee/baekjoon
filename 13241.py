a, b = map(int, input().split())
# print(a*b)
tmp=a*b

if a<b:
    for i in range(b, 0, -1):
        if a% i == 0 and b%i==0:
            print((a//i) * (b//i)* i)
            break
else:
    for i in range(a, 0, -1):
        if a% i == 0 and b%i==0:
            print((a//i) * (b//i)* i)
            break
