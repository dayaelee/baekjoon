import sys
input = sys.stdin.readline
arr=[]
n = int(input())
for i in range(n):
    arr.append(list(input().strip()))

answer = 0
dic={}
key = ['C', 'P', 'Z', 'Y']
for i in key:
    dic[i]=1

for i in range(n): # 가로 
    start = arr[i][0]
    cnt=1
    for j in range(1, n):
        if start == arr[i][j]:
            cnt+=1
        else:
            if dic[start]<=cnt:
                dic[start]=cnt
            cnt = 1
            start=arr[i][j]
    if dic[start]<=cnt:
        dic[start]=cnt
    
    # print(dic)
    answer = max(max(dic.values()), answer)
    for q in key:
        dic[q]=1

# print(answer)

for i in range(n): #세로 
    start = arr[0][i]
    cnt=1
    for j in range(1, n):
        if start == arr[j][i]:
            cnt+=1
        else:
            if dic[start]<=cnt:
                dic[start]=cnt
            cnt=1
            start=arr[j][i]
    if dic[start]<=cnt:
        dic[start]=cnt
    #print(dic)
    answer = max(max(dic.values()), answer)
    for i in key:
        dic[i]=1

# print(answer, '??')

for j in range(n): # 위아래 변경 
    for i in range(n-1):
        if arr[i][j] != arr[i+1][j]:
            arr[i][j], arr[i+1][j]= arr[i+1][j], arr[i][j] # 바꾸기 

            start1 = arr[i][0]
            cnt1=1
            start2 = arr[i+1][0]
            cnt2=1
            for k in range(1, n):
                if arr[i][k]==start1:
                    # dic[start1]+=1
                    cnt1+=1
                else:
                    if dic[start1]<cnt1:
                        dic[start1]=cnt1
                    cnt1=1
                    start1=arr[i][k]
            if dic[start1]<cnt1:
                dic[start1]=cnt1
            answer = max(max(dic.values()), answer)
            # print(dic, '1i: ', i, 'j: ', j)
            for q in key:
                dic[q]=1
            
            # print('dic!', dic)
            for k in range(1, n):
                #print('arr[i+1][k]==start2', arr[i+1][k], start2)
                if arr[i+1][k]==start2:
                    cnt2+=1
                else:
                    if dic[start2]<cnt2:
                        dic[start2]=cnt2
                    cnt2=1
                    start2=arr[i+1][k]
            if dic[start2]<cnt2:
                dic[start2]=cnt2
            answer = max(max(dic.values()), answer)
            # print(dic, '2i: ', i, 'j: ', j)
            for q in key:
                dic[q]=1

            start1 = arr[0][j]
            cnt1=1
            
            for k in range(1, n):
                if arr[k][j]==start1:
                    
                    cnt1+=1
                else:
                    if dic[start1]<cnt1:
                        dic[start1]=cnt1
                    cnt1=1
                    start1=arr[k][j]
            if dic[start1]<cnt1:
                dic[start1]=cnt1
            answer = max(max(dic.values()), answer)
            # print(dic, '3i: ', i, 'j: ', j)
            for q in key:
                dic[q]=1        
            
            arr[i][j], arr[i+1][j]= arr[i+1][j], arr[i][j] # 원상복구
    
# print()
for i in range(n): # 좌우 변경 
    for j in range(n-1):            
        if arr[i][j] != arr[i][j+1]:
            arr[i][j], arr[i][j+1]= arr[i][j+1], arr[i][j] # 바꾸기 
            start1 = arr[0][j]
            cnt1=1
            start2 = arr[0][j+1]
            cnt2=1
            for k in range(1, n):
                if arr[k][j]==start1:
                    cnt1+=1
                else:
                    if dic[start1]<cnt1:
                        dic[start1]=cnt1
                    cnt1=1
                    start1=arr[k][j]
            if dic[start1]<cnt1:
                dic[start1]=cnt1
            answer = max(max(dic.values()), answer)
            # print(dic, '1i: ', i, 'j: ', j)
            for q in key:
                dic[q]=1        
                
            for k in range(1, n):
                if arr[k][j+1]==start2:
                    
                    cnt2+=1
                else:
                    if dic[start2]<cnt2:
                        dic[start2]=cnt2
                    cnt2=1
                    start2=arr[k][j+1]
            if dic[start2]<cnt2:
                dic[start2]=cnt2
            answer = max(max(dic.values()), answer)
            # print(dic, '2i: ', i, 'j: ', j)
            for q in key:
                dic[q]=1   
                
            start1 = arr[i][0]
            cnt1=1
            for k in range(1, n):
                if arr[i][k]==start1:
                    cnt1+=1
                else:
                    if dic[start1]<cnt1:
                        dic[start1]=cnt1
                    cnt1=1
                    start1=arr[i][k]
            if dic[start1]<cnt1:
                dic[start1]=cnt1
            answer = max(max(dic.values()), answer)
            # print(dic, '3i: ', i, 'j: ', j)
            for q in key:
                dic[q]=1
            arr[i][j], arr[i][j+1]= arr[i][j+1], arr[i][j] # 원상복구
print(answer)