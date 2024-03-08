# 거듭제곱
# 숫자 N, M 이 주어질 때, N의 M 거듭제곱 값을 구하는 프로그램을 재귀호출을 이용하여 구현.
# 총 10개의 테스트 케이스, 결과 값은 integer 범위를 넘어가지 않음.
# input 예시
# 1
# 9 8
# 2
# 2 8

## 1번 방법
for _ in range(10):
    case = int(input())
    m, n = map(int, input().split())

    def power(m,n):
        if n == 1:
            return m
        return m * power(m, n-1)

    print(f'#{case}', power(m,n))


## 2번 방법
def square(m, n):
    if n == 1:
        return m
    return m * square(m, n-1)


for _ in range(10):
    try:
        number = input()
        numbers = input()
        m, n = map(int, numbers.split())
        print(f'#{number}', square(m,n))
    except ValueError:
        break


# number = input()
# numbers = input()
# number2 = input()
# numbers2 = input()
#
# m,n = map(int,numbers.split())
# p,q = map(int,numbers2.split())

# print(m,n)

# print(f'#{number}', square(m,n))
# print(f'#{number2}', square(p,q))

