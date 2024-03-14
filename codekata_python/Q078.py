# 접두사인지 확인하기
# 접두사 - 특정 인덱스까지의 문자열
# my_string과 is_prefix가 주어질 때, is_prefix가 my_string의 접두사라면 1, 아니면 0을 return


def solution(my_string, is_prefix):
    if my_string[0:len(is_prefix)] == is_prefix:
        return 1
    else:
        return 0


print(solution("banana", "ban"))
print(solution("banana", "nan"))
print(solution("banana", "abcd"))
print(solution("banana", "bananan"))