# 삼각형의 완성 조건
# 가장 긴 변의 길이는 다른 두 변의 합보다 길어야 함
# 세 변의 길이 sides
# 삼각형 가능하면 1, 아니면 0 return


def solution(sides):
    sides.sort()
    if sides[2] >= sides[0] + sides[1]:
        return 2
    elif sides[2] < sides[0] + sides[1]:
        return 1


print(solution([1,2,3]))
print(solution([3,6,2]))
print(solution([199,72,222]))