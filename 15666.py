
n, m = map(int, input().split())
nlist = list(set(list(map(int, input().split()))))

nlist.sort() # 오름차순
answer=[]
def recursion(cnt, limit, answer):

    if cnt==limit:
        print(' '.join(map(str, answer)))
        return 

    for i in range(0, len(nlist)):
        if answer:
            if answer[-1]<=nlist[i]:
                answer.append(nlist[i])
                recursion(cnt+1, limit, answer)
                answer.pop()
        else:
            answer.append(nlist[i])
            recursion(cnt+1, limit, answer)
            answer.pop()


recursion(0, m, answer)


