tt = []

for i in range(0,3):
    tt.append(0)

tt[0], tt[1], tt[2]= map(int, input().split(" "))

tt.sort()
print(tt)

while 1:
    if tt[2] >= tt[0] + tt[1]:
        tt[2] = tt[2]-1
        
    elif tt[2]< tt[0] + tt[1] :
        print(tt[0]+tt[1]+tt[2])
        break

