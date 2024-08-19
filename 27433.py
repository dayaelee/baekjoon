n=int(input())

sum=n
if n==0:
    print(1)
else:

    while 1:
        if n>1:
            n-=1
            sum*=n
        else:
            break
    print(sum)