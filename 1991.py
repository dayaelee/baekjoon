import sys 
from collections import deque
input = sys.stdin.readline

n = int(input())
dic={}
for i in range(n):
    root, left, right = input().split()
    dic[root] = [left, right]

# 전위 순회 
def dfs(start):
    if start !='.':
        print(start, end='')
        dfs(dic[start][0])
        dfs(dic[start][1])
    
dfs('A')
print('')

def mid(start):
    if start!='.':
        mid(dic[start][0])
        print(start, end='')
        mid(dic[start][1])
mid('A')
print()

def post(start):
    if start!='.':
        post(dic[start][0])
        post(dic[start][1])
        print(start, end='')
post('A')
