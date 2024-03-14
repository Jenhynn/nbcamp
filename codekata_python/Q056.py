# 두 수의 연산값 비교하기
# 두 정수를 붙여서 쓴 값을 반환하는 연산.
# a,b 가 주어졌을 때 a (+) b 와 2*a*b 중 더 큰 값을 return. 같으면 a(+)b


def solution(a,b):
    new = int(str(a) + str(b))
    if new >= 2 * a * b:
        return new
    else:
        return 2 * a * b

print(solution(2, 91))
print(solution(91, 2))