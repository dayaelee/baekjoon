m = int(input())
n = int(input())

rangeN = 10000

checkList = [False, False] + [True]*(rangeN-1)
prime=[]

for i in range(0, n+1):
    if checkList[i]==True:
        prime.append(i)
        for j in range(i*2, n+1, i):
            checkList[j]=False

firstn=0
sum = 0
count = 0
for i in range(0, len(prime)):
    if prime[i]>=m and prime[i]<=n:
        if count==0:
            firstn = prime[i]
            count = count+1

        sum=sum+prime[i]
    #print(prime[i])

if sum ==0 and firstn ==0:
    print(-1)
else:

    print(sum)
    print(firstn)