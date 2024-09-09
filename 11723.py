import sys
input = sys.stdin.readline

n = int(input())
tmp = []
for i in range(n):
    entire = input().strip()
    if entire=='all': 
        tmp = list(range(1, 21))
    elif entire=='empty':
        tmp.clear()
    else:
        s, v = entire.split()
        v = int(v)
        if s == 'add':
            if v not in tmp:
                tmp.append(v)
        
        if s == 'check':
            if int(v) in tmp:
                print(1)
            else:
                print(0)
        
        if s == 'remove':
            if v in tmp:
                tmp.remove(v)
        
        if s == 'toggle':
            if int(v) in tmp:
                tmp.remove(v)
            else:
                tmp.append(v)
        
        
