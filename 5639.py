import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
basket=[]
while 1:
    try:
        tmp = int(input())
        basket.append(tmp)
    except:
        break


def post_order(root, last):
    if root >last:
        return
    
    rootNode = basket[root]

    right_start = root+1

    while right_start<=last:
        if basket[right_start] >rootNode:
            break
        right_start+=1
    
    post_order(root+1, right_start-1)

    post_order(right_start, last)

    print(rootNode)

post_order(0, len(basket)-1)