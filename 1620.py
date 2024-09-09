import sys
input = sys.stdin.readline

n, m = map(int, input().split())
dic = {}
revDic = {}
for i in range(n):
    tmpS = input().strip()
    dic[i+1]=tmpS
    revDic[tmpS]=i+1

for i in range(m):
    tmpV = input().strip()
    if tmpV.isdigit():
        tmpV= int(tmpV)
        print(dic[tmpV])
    else:
        print(revDic[tmpV])
