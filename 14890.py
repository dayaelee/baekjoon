import sys
input = sys.stdin.readline

n, l = map(int, input().split())
graph=[]
for i in range(n):
    graph.append(list(map(int, input().split())))


# 가로 먼저
def rowCheck():
    cntRoad = 0
    for i in range(n):
        flag = 0
        exit=0
        for j in range(n):
            if j ==0: # 초기 설정
                cnt=1
                now = graph[i][j]
                continue
                
            if now == graph[i][j]: # 나왔던 수가 나오는 경우 
                cnt+=1
                if flag == 1: # 내려가는 경사로를 신경써야하는 경우
                    if l==cnt:
                        flag = 0
                        cnt = 0
            else:
                if flag==0: 
                    if now +1 == graph[i][j]: # 새로운 수 등장 
                        if cnt >=l: # 그동안 지나온 길이 경사로가 되나? 
                            cnt = 1
                            now = graph[i][j]
                        else: # 안된다 
                            exit=1
                            break # 다음 줄 
                    elif now -1 == graph[i][j]: # 새로운 수 등장
                        flag=1 # 이제 내려가는 경사로 신경써야함
                        now = graph[i][j]
                        if l==1:
                            cnt=0
                            flag=0
                        else:
                            cnt=1
                    else: # 경사로도 못 만듦
                        exit=1
                        break # 다음 줄 
                else:
                    if l == 1:
                        if now -1 == graph[i][j]: # 새로운 수 등장
                            flag=1 # 이제 내려가는 경사로 신경써야함
                            now = graph[i][j]
                            cnt=1
                    else:
                        exit=1
                        break # 다음 줄 
            if j == n-1:
                if flag ==1 and 1<=cnt <l:
                    exit=1
                    break
        if exit==0:
            cntRoad+=1
            print('i', i, '길 인정 받았나? :',cntRoad)
    return cntRoad


def colCheck():
    cntRoad = 0
    for i in range(n):
        flag = 0
        exit=0
        for j in range(n):
            if j ==0: # 초기 설정
                cnt=1
                now = graph[j][i]
                continue
            # print('j: ',j, ' cnt', cnt)
            if now == graph[j][i]: # 나왔던 수가 나오는 경우 
                cnt+=1
                if flag == 1: # 내려가는 경사로를 신경써야하는 경우
                    if l==cnt:
                        flag = 0
                        cnt = 0
            else:
                if flag==0: 
                    if now +1 == graph[j][i]: # 새로운 수 등장 
                        if cnt >=l: # 그동안 지나온 길이 경사로가 되나? 
                            cnt = 1
                            now = graph[j][i]
                        else: # 안된다 
                            exit=1
                            break # 다음 줄 
                    elif now -1 == graph[j][i]: # 새로운 수 등장
                        flag=1 # 이제 내려가는 경사로 신경써야함
                        now = graph[j][i]
                        if l==1:
                            cnt=0
                            flag=0
                        else:
                            cnt=1
                    else: # 경사로도 못 만듦
                        exit=1
                        break # 다음 줄 
                else:
                    exit=1
                    break # 다음 줄 
            if j == n-1:
                if flag ==1 and 1<=cnt <l :
                    exit=1
                    break
        if exit==0:
            cntRoad+=1
            print('i', i, '길 인정 받았나? :',cntRoad)
    return cntRoad

answer = 0
answer+=rowCheck()
print()
answer+=colCheck()
print(answer)