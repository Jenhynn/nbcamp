#피자 나눠 먹기

def solution(n):
    if n % 7 == 0:
        answer = n//7
    else:
        answer = n//7 + 1
    return answer

print(solution(15))
