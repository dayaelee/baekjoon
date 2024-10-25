import heapq

n = int(input())
value = []
for i in range(n):
    value.append(int(input()))

heapq.heapify(value)
result = 0
if n == 1:
    result=0
else:
    while 1:
        if len(value) == 1:
            break
        one = heapq.heappop(value)
        two = heapq.heappop(value)
        tmp = one+two
        result += tmp

        heapq.heappush(value, tmp)

print(result)
