import itertools

s=list(input())
sn=len(s)

total=[]
for i in range(sn):

    for cnt in range(1, sn+1):
        tmp=''
        if i+cnt<=sn:
            
            tmp=s[i:i+cnt]
        # print('tmp', tmp)
        if len(tmp)>=1:
            total.append(''.join(tmp))
# print(total)
print(len(set(total)))
