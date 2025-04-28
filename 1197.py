import sys
input = sys.stdin.readline

v, e = map(int, input().split())
graph=[]
root = [i for i in range(v+1)]
for i in range(e):
    graph.append(list(map(int, input().split())))

graph.sort(key=lambda x: x[2])

def find(x):
    if x != root[x]:
        root[x] = find(root[x])
    return root[x]

answer=0
for a, b, c in graph:
    ar = find(a)
    br = find(b)

    if ar!=br:
        if ar>br:
            root[ar]=br
        else:
            root[br]=ar
    
        answer+=c
print(answer)
