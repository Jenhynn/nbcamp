#특정 문자 제거하기

def solution(my_string, letter):
    new_str = my_string.replace(letter, '')
    return new_str

print(solution('abcdef', 'f'))