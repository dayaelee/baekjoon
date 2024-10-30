'''
갖고있는 자연수 카드 수 n장
i번 카드엔 ai가 쓰여져 있음

카드 합체 놀이 = 카드들을 합체하며 노는 놀이 

1. x번 카드와 y번 카드를 골라 그 두 장에 쓰여진 수를 더한 값을 계산한다. (x ≠ y)
2. 계산한 값을 x번 카드와 y번 카드 두 장 모두에 덮어 쓴다.

카드 합체를 총 m번 하면 놀이가 끝남

이때, n장의 카드에 쓰여있는 수를 모두 더한 값이 이 놀이의 점수가 됨

이 점수를 가장 작게 만드는 것이 놀이의 목표 



'''

import heapq

n, m = map(int, input().split())


tmp = list(map(int, input().split()))

heapq.heapify(tmp)
print(tmp)

if m !=0:
    for i in range(m):
        one = heapq.heappop(tmp)
        two = heapq.heappop(tmp)
        print('one, two', one, two, 'tmp', tmp)
        summ=one+two
        heapq.heappush(tmp, summ)
        print('be', tmp)
        heapq.heappush(tmp, summ)
        print('be', tmp)
        print('af', tmp)
        print('')

print(tmp)
print(sum(tmp))

