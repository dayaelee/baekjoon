n = int(input())
tmp = list(map(int, input().split()))

tmpSorted = sorted(list(set(tmp)))
#print(tmpSorted)



cnt=0
dic ={}
for i in tmpSorted:
    dic[i] = cnt
    cnt+=1

print(dic)
result = []
for i in tmp:
    result.append(dic[i])
print(' '.join(map(str, result)))