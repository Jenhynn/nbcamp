#분해합
#N과 N을 이루는 각 자리수의 합
#생성자가 여러 개일 수도, 없을 수도 있음.
#가장 작은 생성자를 구해내는 프로그램 작성하기


def digitsum(n):
    num = int(n)
    if num < 10:
        return num
    else:
        result = num % 10 + digitsum(num//10)
    return result + n



print(digitsum(234)) # 234 + 2 +3 + 4+ 23
