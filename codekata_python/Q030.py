#양꼬치

def solution(n,k):
    if n // 10 >= 1:
        result = 12000 * n + 2000 * (k-n//10)
    else:
        result = 12000 * n + 2000 * k
    return result

print(solution(10,3))
print(solution(64,6))