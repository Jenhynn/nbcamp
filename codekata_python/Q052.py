# 문자열의 뒤의 n글자
# my_string의 뒤의 n글자로 이루어진 문자열을 return


def solution(my_string, n):
    length = len(my_string)
    answer = my_string[length-n:length]
    return answer

print(solution("ProgrammerS123", 11))
print(solution("He110W0r1d", 5))