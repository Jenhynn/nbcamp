# 소문자로 바꾸기
# 알파벳으로 이루어진 문자열 myString. 모든 알파벳을 소문자로 변환하여 return


def solution(myString):
    answer = myString.lower()
    return answer


print(solution("aBcDeFg"))
print(solution("aaa"))