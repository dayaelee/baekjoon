import itertools
import sys
to = int(input())

m = int(input())
able = []
ableB = [True] * 10
if m:
    eList = list(map(int, input().split()))
    if to == 100:
        print(0)
        sys.exit(0)
    else:

        for i in eList:
            ableB[i]=False

if to ==100:
    print(0)
else:
    for i in range(10):
        if ableB[i]==True:
            able.append(i)
    # print('^^', able)


    # 바로 100이 나오는 경우 - 조회할 필요 없음
    result = 0
    # print(len(str(to)))
    first = [(1, 0, 0)]+list(itertools.product(able, repeat=len(str(to)))) 
    # result +=len(str(to)) # 초기 값 
    # print('hi', first)

    print(result)

    global press
    press = float("inf")
    global fin

    for i in first:
        target = int("".join(map(str, i)))
        
        print('??',target,i, result)
        if target < to:
            if press>= to-target:
                press=to-target
                fin = target
                result= len(str(int("".join(map(str, i)))))
                if target ==100:
                    result =0
            else:
                continue
        elif target == to:
            press = 0
            print(result)
            fin = target
            result= len(str(int("".join(map(str, i)))))
            if target ==100:
                    result =0
            break
        else: # i > to
            if press >= target-to:
                press= target-to
                fin = target
                result= len(str(int("".join(map(str, i)))))
                if target ==100:
                    result =0
            else:
                break
            
    print('fin', fin, 'press', press)
    print(result, press)
    print(result+press)