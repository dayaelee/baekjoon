
n=list(map(int, list(input())))

n.sort(reverse=True)
# print(n)
if int(''.join(map(str, n)))%30==0:
    print(int(''.join(map(str, n))))
else: 
    print(-1)



