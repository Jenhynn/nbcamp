# n의 배수
# 정수 num, n 이 매개변수 num이 n의 배수이면 1, n의 배수가 아니라면 0을 return


def solution(num, n):
    if num % n == 0:
        return 1
    else:
        return 0


print(solution(98,2))
print(solution(34,3))