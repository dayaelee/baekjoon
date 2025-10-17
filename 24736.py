a = list(map(int, input().split()))
b = list(map(int, input().split()))

s = [6, 3, 2, 1, 2]

s1, s2 = 0,0 

for i in range(5):
    s1+=a[i]*s[i]
    s2+=b[i]*s[i]

print(s1, s2)