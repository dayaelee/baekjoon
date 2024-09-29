
n, l = map(int, input().split()) # 첫째 줄에 물이 새는 곳의 개수 N, 테이프의 길이 L
mapp = list(map(int, input().split())) # 물이 새는 곳의 위치

# mapp 을 오름차순으로 정렬시켜야함
newMap = sorted(mapp)
result = 0

tmp = l
for i, value in enumerate(newMap):
    if i == len(newMap)-1:
          if l>=tmp:
                result +=1
          break
    
    if tmp <=0 or tmp-(newMap[i+1]-newMap[i])<=0:
            result+=1
            tmp=l
    elif tmp-(newMap[i+1]-newMap[i])>0:
          tmp-=newMap[i+1]-newMap[i]

    if tmp <=0:
        result+=1
        tmp=l

print(result)
