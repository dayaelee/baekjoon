# a, b, v = map(int, input().split())

# day=0
# namuge=0

# day = (v//(a-b))
# namuge= (v%(a-b))
# print("day",day)


# if day>=1 and namuge ==0:
#     if b==1 and :
#         print(day)
#     else:
#         print(day-b)

# elif day>=1 and namuge !=0 and namuge>b:
#     print(day+1)
# elif day>=1 and namuge !=0 and namuge<b:
#     print(day)
A, B, V = map(int, input().split())
if (V-B)%(A-B) == 0:
    print ((V-B)//(A-B))
else:
    print ((V-B)//(A-B)+1)