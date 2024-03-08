# 단어 추출
# 어디에 단어가 들어갈 수 있을까
# N×N 크기의 단어 퍼즐을 만들 때, 주어진 퍼즐 모양에서 특정 길이 K인 단어가 들어갈 수 있는 자리의 수를 출력
# 5<=N<=15, 2<=K<=N 인 정수.
# 첫 줄은 총 테스트 케이스, 테스트 케이스의 첫번째 줄에는 N, K, 두번째 줄부터는 2차원으로 퍼즐의 모양. 흰색 부분이 1, 검은색이 0

t = int(input())
count = 0

for test_case in range(t):
    n, k = map(int, input().split())
    for i in range(1, n+1): #input 된 줄마다 돌면서 공백을 지워 줌
        a = input().replace(' ', '')
        print(a)
        for j in range(1, n-k+1): #각 줄에서 k만큼의 1을 확인해야 함. '1'*(k+1), (k+2) .. 있어도 안 됨. 1*k의 최댓값은 1*n 이니까 (n), (n-1)... (k+1) 등은 안 되는 것.
            if '1'*k in a:
                print('1'*(k+j))
                if '1'*(k+j) in a:
                    print('안됨')
                else:
                    print('됨')
                    # count += 1


        # if '1'*k in a:
        #     print('yes')

    #         if a[j:j+k] == '1'*k:
    #             count += 1
    #         else:
    #             count = count
    # print(count)




