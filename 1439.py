s=list(map(int, input()))
cnt, cnt1, cnt0=0, 0, 0
n=len(s)
flag1=0
flag0=0

while(cnt<n):
    if cnt==0:
        if s[cnt]==0:
            flag0=1
            cnt0+=1
        else:
            flag1=1
            cnt1+=1
    else:
        if flag0==1:
            if s[cnt]==0:
                pass
            else:
                cnt1+=1
                flag0=0
                flag1=1
        elif flag1==1:
            if s[cnt]==1:
                pass
            else:
                cnt0+=1
                flag0=1
                flag1=0
    
    cnt+=1

print(min(cnt0, cnt1))
