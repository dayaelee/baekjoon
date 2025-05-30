import sys
input = sys.stdin.readline

def recursion(N, tmp, start, end, turn):
    if end-start<=1:
        if turn==0:
            cnt=N//3
            if n==1 and cnt==0:
                a='-'
                b=' '
                c='-'
                return a+b+c
            elif n==0 and cnt==0:
                return '-'
        else:
            return tmp

    cnt=N//3    
    a=recursion(cnt, tmp[:cnt], start, start+cnt,turn+1)
    b=[' ']*cnt
    c=recursion(cnt, tmp[-cnt:], start+cnt+cnt, end,turn+1)
    return a+b+c


while 1:
    try:
        n = int(input())
        tmp = ['-'] * (3**n)
        print(''.join(recursion(3**n, tmp, 0, 3**n, 0)))
    except :
        break