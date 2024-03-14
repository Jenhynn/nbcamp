# 공배수
# 정수 number와 n,m. number가 n의 배수이면서 m의 배수이면 1, 아니라면 0


def solution(number, n, m):
    if number % n == 0 and number % m == 0:
        return 1
    else:
        return 0


print(solution(60, 2, 3))
print(solution(55, 10, 5))