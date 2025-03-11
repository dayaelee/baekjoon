n, m = map(int, input().split())
nList = list(map(int, input().split()))
nList.sort()
# global start
start = 0
basket = []
visited = [False] * n
result=set()
def backtrack(cnt, start, result):
    if start == cnt:
        tBasket = tuple(basket)
        if tBasket not in result:
            result.add(tBasket)
            print(' '.join(map(str, basket)))
            return result

    for i in range(len(nList)):
        if visited[i] == False:
            if start<cnt:
                visited[i] = True
                start+=1
                basket.append(nList[i])
                
                result = backtrack(cnt, start, result)
                basket.pop()
                start-=1
                visited[i] = False
    return result

backtrack(m, start, result)