# A의 수만 재배열
n = int(input())
a = sorted(list(map(int, input().split())), reverse=True)
b = list(map(int, input().split()))

dic = {}

sb = sorted(b)
for i in range(len(b)):
    dic[i]=sb[i]

total=0
print(a)
for i in range(len(a)):
    total+=dic[i]*a[i]

print(dic)
print(total)