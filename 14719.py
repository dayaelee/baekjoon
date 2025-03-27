h, w = map(int, input().split())
world = list(map(int, input().split()))

answer = 0
for i in range(1, len(world)-1):
    left=world[:i]
    right = world[i+1:]
    lmax=max(left)
    rmax=max(right)
    minn = min(lmax, rmax)
    if minn>world[i]:
        answer+=minn-world[i]
print(answer)         
