# 수 조작하기 1
# 정수 n과 문자열 control. control은 'w','a','s','d'로 이루어져있고 앞에서부터 순서대로 n의 값을 바꿈.
# w 은 n + 1, s = n - 1, d = n+10, a = n-10


def solution(n, control):
    for i in range(len(control)):
        if control[i] == 'w':
            n = n+1
        elif control[i] == 's':
            n = n-1
        elif control[i] == 'd':
            n = n+10
        elif control[i] == 'a':
            n = n-10
    return n

print(solution(0, "wsdawsdassw"))