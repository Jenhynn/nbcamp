# 조건에 맞게 수열 변환하기 1
# 정수 배열 arr의 각 원소에 대해 값이 50보다 크거나 같은 짝수라면 2로 나누고 50보다 작은 홀수라면 2를 곱한다. 그 결과인 정수 배열을 return


def solution(arr):
    answer = []
    for i in arr:
        if i % 2 == 0 and i >= 50:
            answer.append(i/2)
        elif i % 2 == 1 and i <50:
            answer.append(i*2)
        else:
            answer.append(i)
    return answer


print(solution([1, 2, 3, 100, 99, 98]))