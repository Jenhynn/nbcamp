#짝수의 합


def solution(n):
    num = 0
    for i in range(2, n+1, 2):
        num = num + i
    return num


print(solution(10))
print(solution(4))