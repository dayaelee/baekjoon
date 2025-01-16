# ==>> 그리디로 풀기 
n = int(input())
all = list(map(int, input().split())) # 도로의 길이 n-1개
price = list(map(int, input().split())) # 주유소의 리터당 가격 n개
total=0
cnt=0
summ=0
real=0
for i in all:
    summ+=i
for i in range(0, n):
    if i<=n-2:
        if real>1:
            real-=1
            continue
        else:
            if price[i+1]<=price[i]:
                total+=price[i]*all[cnt]
                summ-=all[cnt]
                cnt+=1
            else:
                if summ>0:
                    real=1
                    for k in range(i+1, n):
                        if price[i]<price[k]:
                            if k==n-1:
                                break
                            real+=1
                        else:
                            break

                    for kk in range(real):
                        total+=price[i]*all[cnt]
                        summ-=all[cnt]
                        cnt+=1
print(total)