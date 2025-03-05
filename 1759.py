l, c = map(int, input().split()) # l 개, c개의 문자
words = sorted(input().split())
# 최소 한 개의 모음(a, e, i, o, u), 최소 두 개의 자음으로 구성
# 증가하는 순으로 배열

m = ['a', 'e', 'i', 'o', 'u']
global result
result = 0

basket=[]
def backtrack(now, cnt, basket):
    global result
    if cnt == l:
        check = 0
        check2 = 0
        for i in basket:
            if check == 0:
                if i in m:
                    check+=1
            if check2 <= 1:
                if i not in m:
                    check2+=1
            if check == 1 and check2==2:
                print(''.join(basket))
                return 
            
    for i in range(now, len(words)):
        basket.append(words[i])
        result = backtrack(i+1, cnt+1, basket)
        basket.pop()
    return 

backtrack(0, 0, basket)

