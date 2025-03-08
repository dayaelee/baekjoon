n = int(input())

print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")

a="\"재귀함수가 뭔가요?\""
b="\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\""
c="마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지."
d="그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\""
g="\"재귀함수는 자기 자신을 호출하는 함수라네\""
e="라고 답변하였지."

f="____"

tmp=[a, b, c, d, g, e]
global end
end = 0
def recursion(cnt):
    global end
    if end ==0:
        for j in range(len(tmp)):
            if cnt >=1:
                tmp[j] = f + tmp[j]

    for j in range(len(tmp)):
        if cnt == n:
            if j ==0 or j == 4 or j == 5:
                print(tmp[j])
                end = 1
        else:
            if end ==1:
                if j == 5:
                    print(tmp[j][4:])
                    tmp[j]=tmp[j][4:]
                
            else:
                print(tmp[j])
            if j == 3:
                recursion(cnt+1)

            
recursion(0)