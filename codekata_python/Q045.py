# flag에 따라 다른 값 반환하기
# 두 정수 a,b 와 boolean 변수 flag. flag가 true이면 a+b, false이면 a-b 를 return


def solution(a,b,flag):
    if flag == 1:
        return a+b
    elif flag == 0:
        return a-b


print(solution(-4,7,True))
print(solution(-4,7, False))