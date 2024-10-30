from collections import deque
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))



start = 0

result = deque()
i, j = 0, 0
while 1:
    if i < len(a) and j< len(b):

        if a[i]> b[j]:
            result.append(b[j])
            j+=1
        else:
            result.append(a[i])
            i+=1
    else:
        break

result+=a[i:]
result+=b[j:]
            
print(' '.join(map(str, result)))