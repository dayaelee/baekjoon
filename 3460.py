t=int(input())

def divFunc(value, cnt, answer):
    if value == 1:
        answer.append(cnt)
        return answer
    result, rest = divmod(value, 2)
    if rest == 1:
        answer.append(cnt)
    return divFunc(result, cnt+1, answer)

for i in range(t):
    n=int(input())
    print(' '.join(map(str, divFunc(n, 0, []))))
    