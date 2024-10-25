mapp=[]
n, m = map(int, input().split())
for i in range(n):
    mapp.append(input())

tmp = ['W', 'B']
realCNT=1e9
for j in range(m-8+1): # 가로로 이동 
    for k in range(n-8+1): # 세로로 이동 

        for qq in range(2):
            if qq==0:
                start1=tmp[0]
                start2=tmp[1]
            elif qq==1:
                start1=tmp[1]
                start2=tmp[0]    
            cnt1 = 0
            cnt = 0
            for ix in range(0+k, 0+8+k): # 8개 세로세로
                cnt2 = 0
                for i in range(0+j, 0+8+j): # 8개 가로가로
                    if cnt1%2==0: #짝수 
                        if cnt2%2==0: #짝수 
                            if mapp[ix][i]==start1:
                                cnt2+=1
                                continue
                            else:
                                cnt+=1
                        else: # 홀수 
                            if mapp[ix][i]==start2:
                                cnt2+=1
                                continue
                            else:
                                cnt+=1 
                    else: # 홀수 
                        if cnt2%2==0: # 짝수
                            if mapp[ix][i]==start2:
                                cnt2+=1
                                continue
                            else:
                                cnt+=1
                        else: # 홀수 
                            if mapp[ix][i]==start1:
                                cnt2+=1
                                continue
                            else:
                                cnt+=1

                    cnt2+=1
                cnt1+=1   

            if realCNT>cnt:
                realCNT=cnt
print(realCNT)