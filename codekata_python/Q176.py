# 간단한 논리 연산
# boolean 변수 x1, x2, x3, x4 가 주어질 때 (x1 ∨ x2) ∧ (x3 ∨ x4) 식의 true, false 를 return


def solution(x1, x2, x3, x4):
    x = x1 | x2
    y = x3 | x4
    return x & y


print(solution(False, True, True, True))
print(solution(True, False, False, False))