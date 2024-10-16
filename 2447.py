'''
별찍기 

n이 27이면 

크기 27의 패턴은 
공백으로 채워진 가운데의 9*9 정사각형을 크기 9의 패턴으로 둘러싼 형태이다. 
예를 들어 크기 27의 패턴은 다음과 같다. 

크기 9의 패턴은 
공백으로 채워진 가운데의 3*3 정사각형을 크기 3의 패턴으로 둘러싼 형태이다. 
예를 들어 크기 9의 패턴은 다음과 같다. 

*********        
* ** ** *        
*********        
***   ***      
* *   * *       
***   ***       
*********        
* ** ** *         
*********     

크기 3의 패턴은
공백으로 채워진 가운데의 1*1 정사각형을 크기 1의 패턴으로 둘러싼 형태이다. 
예를 들어 크기 3의 패턴은 다음과 같다.

***
* *
***

크기 1의 패턴은 

*

n을 몫이 1이 나올 때 까지 나누면
예를 들어 27의 경우, 

27/3 = 9
9/3 = 3
3/3 = 1 



'''
n = int(input())


# cnt=0
# while n>=3:
#     n = n//3
#     cnt+=1
#     if n==1:
#         break

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



