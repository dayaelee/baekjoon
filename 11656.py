s = input()

tmp = []

for i in range(len(s)):
    tmp.append(s[i:])

tmp = sorted(tmp)
for i in tmp:
    print(i)