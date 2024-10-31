'''

한 사이트에는 최대 한 개의 다리만 연결될 수 있음
다리를 최대한 많이 지으려고 한다. 

서쪽 + 동쪽을 연결하고 싶다. 

서쪽의 사이트 개수만큼 다리를 지으려고 한다. 
다리끼리는 서로 겹칠 수 없다. 

'''
import math
import sys
input = sys.stdin.readline

t = int(input())
for i in range(t):
    n, m = map(int, input().split())

# 29개 중에서 13개 뽑는 경우는? 
    if n == 0:
        print(0)
    else:
        value = math.factorial(m)//(math.factorial(n)*math.factorial(math.factorial(m-n)))
        print(value)