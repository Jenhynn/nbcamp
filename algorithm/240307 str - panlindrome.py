# 문자열 다루기 - 회문
# 회문
# 8×8에서 제시된 길이를 가진 회문의 개수 구하기
# 찾아야 하는 회문의 길이와 글자판이 주어진다.
# 테스트 케이스 번호와 찾은 회문의 개수 출력 : #번호 회문개수

t = int(input())

row_count = 0
col_count = 0

for i in range(8):
    row = input()
    for j in range(8-t+1):
        strings = row[j:j+t]
        if strings == strings[::-1]:
            row_count += 1
            print('회문!', row_count)
        print(strings)
    print('한줄 끝')


