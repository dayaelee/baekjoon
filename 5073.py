
while 1:
    tt = []
    for i in range(0,3):
        tt.append(0)
    
    tt[0], tt[1], tt[2] = map(int, input().split(" "))
    
    if(tt[0]==tt[1]==tt[2]==0):
        break

    tt.sort()


    if tt[0] == tt[1] == tt[2]:
        print("Equilateral")
    elif tt[0]==tt[1]!=tt[2]or tt[0]!=tt[1]==tt[2] or tt[0]==tt[2]!=tt[1]:
        if tt[2] >= tt[0] + tt[1]:
            print("Invalid")
        else:
            print("Isosceles")
        
    elif tt[0]!=tt[1]!=tt[2]:
        if tt[2] >= tt[0] + tt[1]:
            print("Invalid")
        else:
            print("Scalene")
    else:
        if tt[2] >= tt[0] + tt[1]:
            print("Invalid")
    
