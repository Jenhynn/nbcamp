# 배열에서 문자열 대소문자 변환하기
# 문자열 배열 strArr에서 배열에서 홀수번째 인덱스의 문자열은 모든 문자를 대문자로, 짝수번째 문자열은 소문자로 바꿔서 반환


def solution(strArr):
    for i in range(len(strArr)):
        if i % 2 == 1:
            strArr[i] = strArr[i].upper()
        elif i % 2 == 0:
            strArr[i] = strArr[i].lower()

    return strArr


print(solution(["AAA","BBB","CCC","DDD"]))
print(solution(["aBc","AbC"]))
