t = int(input())

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a 

for i in range(t):
    n=list(map(int,input().split()))
    nlen=n[0]
    tmp = n[1:]
    answer=0
    for i in range(nlen-1):
        for j in range(i+1, nlen):
            answer+=gcd(tmp[i], tmp[j])
    print(answer)
