# 홀짝에 따라 다른 값 반환하기
# 양의 정수 n 이 홀수라면 n 이하의 홀수인 모든 양의 정수의 합을 return, n이 짝수라면 n 이하의 짝수인 모든 양의 정수의 제곱의 합을 return


def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(1, n+1, 2):
            answer += i
    if n % 2 == 0:
        for i in range(2, n+1, 2):
            answer += i ** 2
    return answer


print(solution(7))
print(solution(10))