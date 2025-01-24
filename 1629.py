a, b, c = map(int, input().split())

def ppow(a, b):
    if b==1:
        return (a%c)
    else:
        re = ppow(a, b//2)

    if b % 2==0:
        return ((re*re)%c)
    else:
        return ((re*re*a)%c)

if b%2==0:
    print(ppow(a, b))
else:
    if b ==1:
        print(ppow(a, b))
    else:
        print((ppow(a, b)))

# 5 36 * 36
# 2 6*6
# 1 -> 6