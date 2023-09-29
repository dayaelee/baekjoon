n = int(input())

tmp = []
for i in range(0, n):
    tmp.append(0)


for i in range(0, n):
    tmp[i] = int(input())

#print(tmp)

#1센트는 0.01달러 
value = list()
for i in range(0, n):
    tmpp = []
    for j in range(0, 4):
        tmpp.append(0)
    value.append(tmpp)

for i in range(0, n):
    #tmp[i] = tmp[i]*0.01

    #print(tmp)
   
    #value[i][0] = int(tmp[i] // 0.25 )
    
    # value[i][1] =  int((tmp[i] % 0.25) // 0.10)
    
    # #print(((tmp[i] % 0.25) % 0.10))
    # value[i][2] =  int(round(((tmp[i] % 0.25) % 0.10), 2) // 0.05)
    
    # value[i][3] = int(round((round(((tmp[i] % 0.25) % 0.10), 2) % 0.05), 2)//0.01)

    value[i][0] = tmp[i] // 25
    value[i][1] = (tmp[i] % 25) // 10
    value[i][2] = ((tmp[i] % 25) % 10) // 5
    value[i][3] = ((tmp[i] % 25) % 10) % 5


for i in range(0, n):
    print(*value[i])