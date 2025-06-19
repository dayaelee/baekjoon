from collections import deque
import copy
aLimit =list(map(int, input().split()))
a = [0, 0, aLimit[2]]

q = deque([([0, 0, aLimit[2]])])
# q = deque([([2, a])])
visited=[[[0] * (aLimit[2]+1) for _ in range(aLimit[1]+1)] for _ in range(aLimit[0]+1)]
# visited=[[[[0] * (aLimit[0]+1) for _ in range(aLimit[1]+1)] for _ in range(aLimit[2]+1)] for _ in range(3)]
# print(visited)
result = []

visited[0][0][aLimit[2]] = True
#visited[2][aLimit[2]][0][0] = True

while q:
    tmp_1, tmp_2, tmp_3 = q.popleft()
    #where, statusOrigin = q.popleft()
    # print('where, status', where, statusOrigin)

    #tmp_1, tmp_2, tmp_3 = statusOrigin
    statusOrigin=[tmp_1, tmp_2, tmp_3]
    if tmp_1==0:
        result.append(tmp_3)
    
    for i in range(3):
        for j in range(3):
            if i ==j:
                continue
            # if i == where: # 나에게는 안줌 
            #     continue
            status = copy.deepcopy(statusOrigin)
            # mine = status[where]
            if status[i]<aLimit[i]: # 줄 곳이 빈공간이 있네?
                #print()
                # print('i', i, ' 들어 가도 되니? ok', status[where], status[i])
                if status[j]>0: # 줄게 있네?
                    tmp = min(aLimit[i]-status[i], status[j]) # 빈공간 만큼 주거나, 가진것 만큼 주거나 
                    status[j]-=tmp
                    status[i]+=tmp
                    # if tmp >0:
                    #     status[j]= tmp
                    #     status[i]=aLimit[i]
                    #     print('status check!', status)
                    # elif tmp ==0:
                    #     # print('status check!1 - before', status, 'where', where)
                    #     if status[j]+status[i]>aLimit[i]:
                    #         status[j]=(status[j]+status[i])-aLimit[i]
                    #     else:
                    #         status[j]=0
                    #     status[i]=aLimit[i]
                    #     print('status check!1', status)
                    # else:
                    #     # print('status check!2 - before', status, 'where', where)
                    #     if i == j:
                    #         continue
                    #     else:
                    #         status[i]+=status[j]
                    #         status[j]=0
                    #         print('i: ',i, 'status check!2', status)
                        
                    
                    tmp1, tmp2, tmp3 = status[0], status[1], status[2]
                    # print('where', j)
                    # print('tmp1, tmp2, tmp3', tmp1, tmp2, tmp3)
                    if visited[tmp1][tmp2][tmp3]==False:
                    # if visited[i][tmp3][tmp2][tmp1]==False:
                        # print('tmp1, tmp2, tmp3', tmp1, tmp2, tmp3)
                        visited[tmp1][tmp2][tmp3]=True
                        # visited[i][tmp3][tmp2][tmp1]=True
                        q.append((status[0], status[1], status[2]))
                        # q.append((i, status))
                        
                        
            else: # target에 자리 없으면 넘김
                continue

print(' '.join(map(str, sorted(list(set(result))))))
