
n = int(input())


def draw_stars(n):
    if n ==1:
        return ['*']
    
    Stars = draw_stars(n//3)
    L = []

    for star in Stars:
        L.append(star*3)
    for star in Stars:
        L.append(star+' '*(n//3)+star)
    for star in Stars:
        L.append(star*3)
    
    return L
print('\n'.join(draw_stars(n)))



