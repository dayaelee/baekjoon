n = int(input())

a = [False, False] + [True] * (n-1)
primes=[]

for i in range(2, n+1):
    if a[i]: 
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
# print(primes)

answer = 0
for i in range(2, n+1):
    total=0
    if a[i]==True:
        exit=0
        for j in range(i, n+1):
            if a[j]==True:
                # print("?: ", j)
                total+=j
                if total==n:
                    answer+=1
                    break
                elif total>n:
                    break
    # print('answer: ', answer, 'total: ', total)
    # print()

print(answer)