'''
오늘부터 N+1일째 되는 날 퇴사를 하기 위해서, 남은 N일 동안 최대한 많은 상담
비서는 하루에 하나씩 서로 다른 사람의 상담을 잡아놓았다.

각각의 상담은 상담을 완료하는데 걸리는 기간 Ti(일 단위)와 상담을 했을 때 받을 수 있는 금액 Pi로 이루어져 있다.

상담을 하는데 필요한 기간은 1일보다 클 수 있기 때문에, 모든 상담을 할 수는 없다. 

또한, N+1일째에는 회사에 없기 때문에, 6, 7일에 있는 상담을 할 수 없다.
(퇴사 전에 끝낼 수 있는 상담이여야함.)

퇴사 전에 할 수 있는 상담의 최대 이익은 1일, 4일, 5일에 있는 상담을 하는 것이며, 이때의 이익은 10+20+15=45이다.

최대 수익

'''
import sys
input = sys.stdin.readline

n = int(input())
tmp=[]

dp = [ 0 for i in range(n+1)]

for i in range(n):
    t, p = map(int, input().split())
    tmp.append([t, p])

for i in range(n): # i번째까지 일 했을때 얻는 최대 수익 
    for j in range(i+tmp[i][0], n+1): # 
        #print('i:', i, 'j:', j, 'dp[j]',dp[j])
        if dp[j] < dp[i] + tmp[i][1]:
            dp[j] = dp[i] + tmp[i][1]

print(dp[-1])