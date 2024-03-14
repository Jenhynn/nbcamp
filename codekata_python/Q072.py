# 원하는 문자열 찾기
# 알파벳으로 이루어진 문자열 myString과 pat. myString의 연속된 부분 문자열 중 pat이 존재하면 1, 그렇지 않으면 0을 return
# 대문자와 소문자는 구분하지 않음


def solution(myString, pat):
    if pat.lower() in myString.lower():
        return 1
    else:
        return 0


print(solution("AbCdEfG", "aBc"))
print(solution("aaAA", "aaaaa"))