import sys
input = sys.stdin.readline
n=int(input())
point=[]
for i in range(n): # x, y 순임
    point.append(list(map(int, input().split())))
# -번째 포인트는 0번째 포인트로 향함 
#print(point)
answer=0 # 둘레
# 변심거리 
# for a, b in point:
#     a, b = i 
#     round+=(b-a)
# answer =(round )//2
#면적 = 
point.append(point[0])

for i in range(len(point)):
    if i ==0:
        targetA= point[i][0]
    else:
        targetB=point[i][1]
        ###print('?', (targetA*targetB))
        answer+=(targetA*targetB)
        targetA=point[i][0]
        #print('?', targetA,targetB)
#print(answer)

answer2=0
for i in range(len(point)):
    if i ==0:
        targetB= point[i][1]
    else:
        targetA=point[i][0]
        answer2+=(targetA*targetB)
        targetB=point[i][1]
#print(answer2)

print(abs(answer-answer2)/2)