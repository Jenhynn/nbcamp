#자릿수 더하기

def solution(n):
    sumnum = 0
    while n > 10:
        num = n % 10
        sumnum += num
        n = n//10
        if n < 10:
            sumnum += n
            return num, sumnum, n

print(solution(123))


def digitsum(n):
    num = int(n)
    if num < 10:
        return num
    else:
        return num % 10 + digitsum(num//10)

print(digitsum(123))