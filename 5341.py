while(1):

    n = int(input())

    if n==0:
        break
    else:
        ans=0
        for i in range(1, n+1):
            ans+=i

        print(ans)