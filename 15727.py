L = int(input())

t = 0

if L % 5 == 0:
    t = L // 5
else:
    t = (L // 5) + 1

print(t)