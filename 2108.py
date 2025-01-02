import sys
input = sys.stdin.readline

n = int(input())
result = []
dic={}
for i in range(n):
    tmp = int(input())
    result.append(tmp)
    if tmp in dic:
        dic[tmp] += 1
    else:
        dic[tmp] = 1

result.sort()
dic.items() # key, value가 tuple로 들어있는 리스트로 만듦

# 최빈값을 구하고, 그 최빈값을 가진 키 값을 정렬해서 거기서 뒤에서 두번째임



keyList=[]
cnt=0
for key, value in dic.items():
    if value == max(dic.values()):
        cnt+=1
        keyList.append(key)
    
keyList.sort(reverse=True)

# print(sorted(dic.items(), key = lambda x: x[0], reverse=True))
result1 = sorted(dic.items(), key = lambda x: x[0], reverse=True)

result2=sorted(result1, key = lambda x: x[1], reverse=True)
# print(result2)

# print('결과다',result2[0][0])


print(round(sum(result)/n)) # 산술 평균

print(result[len(result)//2]) # 중앙값
if cnt >= 2:
    print(keyList[-2]) # 최빈값 
else:
    print(result2[0][0])
print(max(result)-min(result)) # 범위


