# 문자 반복 출력하기
# 문자열 my_string과 정수 n에서 my_string에 있는 각 문자를 n만큼 반복한 문자열을 return


def solution(my_string, n):
    string = list(my_string)
    repeat =[]
    for i in range(len(string)):
        for j in range(n):
            repeat.append(string[i])
    answer = ''.join(repeat)
    return answer


#다른 사람 풀이 참고: 좀 더 간단한 방법 str으로도 가능
def solution2(my_string, n):
    answer = ''
    string = list(my_string)
    for char in list(my_string):
        answer = answer + char * n
    return string, answer


print(solution("hello",3))
print(solution2("hello",3))