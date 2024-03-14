# 접미사인지 확인하기
# 접미사 - 특정 인덱스부터 시작하는 문자열
# my_string과 is_suffix 주어질 때, is_suffix가 my_string의 접미사라면 1, 아니면 0을 return


def solution(my_string, is_suffix):
    if my_string[-len(is_suffix):] == is_suffix:
        return 1
    else:
        return 0


print(solution("banana", "ana"))
print(solution("banana", "nan"))
print(solution("banana", "wxyz"))
print(solution("banana", "abanana"))
