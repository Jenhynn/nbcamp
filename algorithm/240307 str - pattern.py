# 문자열 다루기 - 패턴 매칭
# 패턴 마디의 길이
# 문자열을 입력 받아 마디의 길이를 출력하는 프로그램 작성.문자열의 길이는 30, 마디의 최대 길이는 10
# 첫 줄에는 테스트 케이스의 개수 T, 그 아래로 테스트 케이스
# 출력 : #t 정답

t = int(input())

for i in range(t):
    string = input()
    for j in range(1, 10):
        if string[:j] == string[j+1:j+1+j]:
            pattern = string[:j+1]
            print(f'#{i+1} {len(pattern)}')
        else:
            continue

# KOREAKOREAKOREA ... 의 경우 패턴이 KOREA 도 도출되고 KOREAKOREA 도 도출됨. 어떻게 해결?