# 글자 이어 붙여 문자열 만들기
# 문자열 my_string, 정수 배열 index_list에서 my_string의 index_list의 원소들에 해당하는 인덱스의 글자들을 순서대로 이어붙인 문자열을 return


def solution(my_string, index_list):
    result = []
    for i in range(len(index_list)):
        j = index_list[i]
        result.append(my_string[j])

    return ''.join(result)

print(solution("cvsgiorszzzmrpaqpe", [16, 6, 5, 3, 12, 14, 11, 11, 17, 12, 7]))
print(solution("zpiaz", [1, 2, 0, 0, 3]))