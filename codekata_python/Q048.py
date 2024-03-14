# 원소들의 곱과 합
# 정수가 담긴 리스트 num_list, 모든 원소들의 곱이 모든 원소들의 합의 제곱보다 작으면 1, 크면 0 return


def solution(num_list):
    answer = 1
    for num in num_list:
        answer *= num
    if answer < sum(num_list) ** 2:
        return 1
    elif answer > sum(num_list) ** 2:
        return 0


print(solution([3, 4, 5, 2, 1]))
print(solution([5, 7, 8, 3]))