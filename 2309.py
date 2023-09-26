n = []
for i in range(0, 9):
    n.append(0)

for i in range(0, 9):
    n[i] = int(input())

n.sort()

sum9 = 0
for i in range(0, 9):
    sum9 = sum9 + n[i]

goal = sum9 - 100
realgoal = goal

end = 0
for i in range(0, 9):
    a = goal - n[i]
    #print("a", a)
    j = 0
    while 1:
        #print("n[",j,"]", n[j], "a", a)

        if n[j] == a:
            if a-n[j]==0:
                n.pop(j)
                n.pop(i)
                end = 1
                break
            else:
                if(j+1==9):
                    break
                else:
                    j = j+1
        else:
            if(j+1==9):
                break
            else:
                j = j+1
 
    if end == 1:
        break
    else:
        goal = realgoal
    

for i in range(0, 7):
    print(n[i])