# n보다 커질 때까지 더하기
# 정수 배열 numbers와 정수 n. numbers의 원소를 앞에서부터 하나씩 더하다가 그 합이 n보다 커지는 순간 이때까지 더했던 원소들의 합을 return


def solution(numbers, n):
    num = 0
    for i in range(len(numbers)):
        num += numbers[i]
        if num > n:
            return num


print(solution([34, 5, 71, 29, 100, 34], 123))
print(solution([58, 44, 27, 10, 100], 139))