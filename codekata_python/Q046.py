# 길이에 따른 연산
# 정수가 담긴 리스트 num_list 리스트의 길이가 11이상이면 원소의 합, 10이하이면 원소의 곱 return


def solution(num_list):
    answer = 1
    if len(num_list) >= 11:
        return sum(num_list)
    elif len(num_list) <= 10:
        for num in num_list:
            answer *= num
        return answer


print(solution([3, 4, 5, 2, 5, 4, 6, 7, 3, 7, 2, 2, 1]))
print(solution([2, 3, 4, 5]))