# 더 크게 합치기
# 연산 (+) 은 두 정수를 붙여서 쓴 값을 반환한다.
# 양의 정수 a와 b가 주어졌을 때 a(+)b 와 b(+)a 중 더 큰 값을 return. 두 값이 같다면 a(+)b 를 return


def solution(a,b):
    ab = int(str(a)+str(b))
    ba = int(str(b)+str(a))
    if ab >= ba:
        return ab
    elif ab < ba:
        return ba


print(solution(9,91))
print(solution(89,8))