'''
축구는 평일 오후에 하고 의무 참석도 아니다.
축구를 하기 위해 모인 사람은 총 N명이고 신기하게도 N은 짝수
N/2명으로 이루어진 스타트 팀과 링크 팀으로 사람들을 나눠야 한다.

사람에게 번호를 1부터 N까지로 배정

능력치 Sij는 i번 사람과 j번 사람이 같은 팀에 속했을 때, 팀에 더해지는 능력치

팀의 능력치는 팀에 속한 모든 쌍의 능력치 Sij의 합이다. 

Sij는 Sji와 다를 수도 있으며, 
i번 사람과 j번 사람이 같은 팀에 속했을 때, 
팀에 더해지는 능력치는 Sij와 Sji

축구를 재미있게 하기 위해서 스타트 팀의 능력치와 링크 팀의 능력치의 차이를 최소로


'''
import sys
import itertools
input = sys.stdin.readline
n = int(input())
s=[]
table = [i for i in range(0, n)]

for i in range(n):
    s.append(list(map(int, input().split())))

'''
중복되지 않게 두개로 나눠 뽑기 



'''
how = n//2
combinations = itertools.combinations(table, how)
minn=1e9
for i in combinations:
    last=[]
    for j in range(n):
        if j not in i:
            last.append(j)
    # print('')
    # print('i', i)
    # print('last', last)

    finalCombiA = itertools.combinations(i,2)
    finalCombiB = itertools.combinations(last, 2)
    summA=0
    summB=0
    for A in finalCombiA:
        ii, jj = A
        summA+=s[ii][jj]
        summA+=s[jj][ii]
    
    for B in finalCombiB:
        ii, jj = B
        summB+=s[ii][jj]
        summB+=s[jj][ii]
    
    if minn>abs(summA-summB):
        minn=abs(summA-summB)

print(minn)