a, b, v = map(int, input().split())

start = 0
now = 0
day = 1

no_one_night_day = (v//(a-b)) -1
print("no_one_night_day",no_one_night_day)

values =  (no_one_night_day * (a-b))+b


print("values",values)
print("     v", v)
count=0

if values>=v:
        print(no_one_night_day)
else:
    while 1:
        if count==0:
            no_one_night_day+=1
            values=values-b
            count=1
        else:
            if values>=v:
                print(no_one_night_day)
                break
            values=values+a 
            if values>=v:
                print(no_one_night_day)
                break
            no_one_night_day+=1
            values=values-b


        
