# 부분 문자열
# 어떤 문자열이 다른 문자열 안에 속하면 부분 문자열
# 문자열 str1이 str2의 부분 문자열이라면 1, 아니라면 0을 return


def solution(str1,str2):
    if str1 in str2:
        return 1
    else:
        return 0


print(solution("abc", "aabcc"))
print(solution("tbt","tbbttb"))