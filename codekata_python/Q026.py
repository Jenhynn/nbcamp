#피자 나눠 먹기

def solution(slice, n):
    if n % slice == 0:
        answer = n//slice
    else:
        answer = n//slice + 1
    return answer

print(solution(7, 10))
print(solution(4,12))