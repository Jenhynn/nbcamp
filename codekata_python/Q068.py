# 조건에 맞게 수열 변환하기 3
# 정수 배열 arr와 자연수 k
# k 가 홀수라면 arr의 모든 수에 k를 곱하고 k가 짝수라면 arr의 모든 원소에 k를 더하여 arr을 return


def solution(arr,k):
    answer = []
    if k % 2 == 1:
        for i in arr:
            answer.append(i*k)
    if k % 2 == 0:
        for i in arr:
            answer.append(i+k)
    return answer


print(solution([1, 2, 3, 100, 99, 98], 3))
print(solution([1, 2, 3, 100, 99, 98], 2))
