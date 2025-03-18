n, b = map(int, input().split())

def result(n, b):
    answer = ''
    while n>0:
        n, mod = divmod(n, b)
        # print(n, mod)
        if mod <10:
            answer+=str(mod)
        else:    
            answer+=str(chr(mod+55))
    return answer[::-1]
print(result(n, b))