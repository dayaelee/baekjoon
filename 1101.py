import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    i = 0
    goal_dis = y-x
    m_dis =0
    cnt = 0
    while 1:
        i+=1
        m_dis += i * 2
        cnt+=2

        if m_dis - i >= goal_dis:
            print(cnt-1)
            break
        elif m_dis >=goal_dis:
            print(cnt)
            break