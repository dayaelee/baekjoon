import sys
input = sys.stdin.readline
n, m = map(int, input().split())
dic={}
for i in range(n):
    key, pw = input().split()
    dic[key]=pw

for i in range(m):
    site = input().strip()
    if site in dic:
        print(dic[site])
