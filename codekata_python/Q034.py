# 짝수는 싫어요
# 매개변수는 정수 n
# n 이하의 홀수가 오름차순으로 담긴 배열을 return


def solution(n):
    answer =[]
    for i in range((n+1)//2):
        answer.append(2 * i + 1)
    return answer

# 다른 사람 풀이 참고: 다른 풀이 참고
def solution2(n):
    return [i for i in range(1,n+1, 2)]

# >> 다시 해석하면
def solution2(n):
    answer =[]
    for i in range(1, n+1, 2):
        answer.append(i)
    return answer


print(solution(10))
print(solution(15))