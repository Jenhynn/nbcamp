# rny_string
# 'm' 과 'rn' 이 모양이 비슷한 점을 이용해 문자열 rny_string의 모든 m을 rn으로 바꾼 문자열을 return


def solution(rny_string):
    if 'm' in rny_string:
        rny_string = rny_string.replace('m', 'rn')
        return rny_string
    else:
        return rny_string



print(solution('masterpiece'))
print(solution('programmers'))
print(solution('jerry'))
print(solution('burn'))