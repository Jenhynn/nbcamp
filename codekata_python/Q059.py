# 홀짝 구분하기
# 자연수 n이 주어졌을 때 n이 짝수이면 "n is even", 홀수이면 "n is odd"를 출력하는 코드를 작성


a = int(input())

if a % 2 == 0:
    print(f'{a} is even')
elif a % 2 == 1:
    print(f'{a} is odd')