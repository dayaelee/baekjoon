
day, a, b = map(int, input().split())

one, two = 1, 1

for i in range(day):
    one +=a
    two +=b

    if one < two:
        tmp = one
        one = two
        two = tmp
    elif one == two:
        two-=1

print(one, two)