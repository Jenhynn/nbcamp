# 모음 제거
# a,e,i,o,u 를 제거한 문자열을 return 하도록


def solution(my_string):
    consonants = []
    string = list(my_string)
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(string)):
        if string[i] not in vowels:
            consonants.append(string[i])
        else:
            continue
    answer = ''.join(consonants)
    return answer


#다른 사람 풀이 참고: list 로 변환하지 않고도 가능
# def solution2(my_string):
#     result = []
#     for char in my_string:
#         if char not in "aeiou":
#             result.append(char)
#     return ''.join(result)


print(solution('bus'))
print(solution('nice to meet you'))