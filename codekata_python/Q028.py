#자릿수 더하기

def solution(n):
    num = int(n)
    if num < 10:
        return num
    else:
        result = num % 10 + solution(num//10)
    return result