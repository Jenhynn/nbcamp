# 좋은 단어 : 3986번
# 단어 위로 아치형 곡선을 그어 A는 A끼리, B는 B끼리 쌍을 지을 때 선 끼리 교차하지 않으면서 짝을 맞출 수 있다면 그 단어는 '좋은 단어'이다.
# 첫째 줄에 단어의 수 N, 다음 줄 부터는 A와 B로만 이루어진 단어가 N줄 주어진다. 단어의 길이는 2 ~ 100,000이며 모든 단어 길이의 합은 1,000,000 이하

n = int(input())

cnt = 0
for i in range(n):
    string = input()
    stack = []
    for char in string:
        if not stack:
            stack.append(char)
        else:
            if stack[-1] == char:
                stack.pop()
            elif stack[-1] != char:
                stack.append(char)

    if not stack:
        cnt += 1

print(cnt)