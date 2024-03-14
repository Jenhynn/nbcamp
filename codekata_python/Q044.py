# 이어 붙인 수
# 정수가 담긴 리스트 num_list, 홀수만 이어붙인 수와 짝수만 이어붙인 수의 합을 return


def solution(num_list):
    even = ''
    odd = ''
    for num in num_list:
        if num % 2 == 0:
            even += str(num)
        elif num % 2 == 1:
            odd += str(num)
    return int(even) + int(odd)


print(solution([3,4,5,2,1]))
print(solution([5,7,8,3]))