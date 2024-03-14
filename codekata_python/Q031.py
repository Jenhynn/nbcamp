# 세균 증식
# 한 시간에 두배만큼 증식
# 처음 세균 수 n마리, 경과한 시간 t시간
# t시간 후 세균의 수 return


def solution(n,t):
    answer = n * (2 ** t) #제곱은 **
    return answer


print(solution(2, 10))
print(solution(7, 15))
