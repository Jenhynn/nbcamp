# 문자열의 앞의 n글자
# 문자열 my_string, 정수 n, 앞의 n글자로 이루어진 문자열 return


def solution(my_string, n):
    answer = my_string[:n]
    return answer


print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))