# 초심자의 회문 검사
# 회문이면 1 출력, 아니라면 0 출력
# 예제 input
# 3
# level
# samsung
# eye

t = int(input())
result = []

for i in range(1, t+1):
    temp = input()
    if temp == temp[::-1]:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')


    # if temp == temp[::-1]:
    #     print('palindrome')
    # else:
    #     print('not palindrome')

