document = input()
find = input()
now = 0
cnt=0
checkpoint=-1
for index, i in enumerate(document):
    if checkpoint > index:
        continue
    now = index
    now2=0
    while 1:
        if now == len(document):
            break
        if document[now] == find[now2]:
            now+=1
            now2+=1
            if now-index == len(find):
                cnt+=1
                checkpoint = now
                break
        else:
            break

print(cnt)