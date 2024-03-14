# 제곱수 판별하기
# 어떤 자연수를 제곱했을 때 나오는 정수 n 이 제곱수
# n이 제곱수라면 1, 아니라면 2 return

import math


def solution(n):
    square_root = n ** (1/2)
    if square_root == int(square_root):
        answer = 1
    else:
        answer = 2
    return square_root, answer


print(solution(144))
print(solution(976))