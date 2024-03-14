# 가위 바위 보
# 가위는 2, 바위는 0, 보는 5
# 가위 바위 보를 내는 순서를 나타낸 문자열 rsp를 모두 이기는 경우를 나타낸 문자열 return


def solution(rsp):
    new_rsp = []
    for i in range(len(rsp)):
        if rsp[i] == '2':
            new_rsp.append('0')
        elif rsp[i] == '0':
            new_rsp.append('5')
        elif rsp[i] == '5':
            new_rsp.append('2')

    return ''.join(new_rsp)


print(solution("2"))
print(solution("205"))
