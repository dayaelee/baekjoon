strr=list(input().split('-'))
#print(strr)
checcking=[]
for i in range(len(strr)):
    if i == 0:
        if '+' not in strr[i]:
            checcking.append(['+' , int(strr[i])])
    else:
        if '+' not in strr[i]:
            checcking.append(['-', int(strr[i])])
        else:
            #print('hi')
            tmp = strr[i].split('+')
            res=0
            for j in tmp:
                res+=int(j)
            #print(tmp)
            checcking.append(['-', res])

if  '+' in strr[0]:
    tmp=strr[0].split('+')
    for j in tmp:
        checcking.append(['+', int(j)])



#print(checcking)


resultS=''
for i in checcking:
    resultS+=i[0]+str(i[1])
print(eval(resultS))

# for i in range(len(strr)):
#     if i%2==0:
#         result.append(eval(strr[i]))
#     else:
#         result.append(-eval(strr[i]))
# print(result)
# resultS=''
# for j in result:
#     resultS+=str(j)
# print(eval(resultS))