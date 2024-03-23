# 외계행성의 나이
# 나이를 알파벳으로 말하는 외계 행성. a:0, b:1, c:2, ..., j:9
# age가 주어졌을 때 외계행성식 나이 return


def solution(age):
    arr = list(map(int, str(age)))
    dict = {0: 'a', 1: 'b', 2: 'c', 3:'d', 4:'e', 5:'f', 6: 'g', 7:'h', 8:'i', 9:'j'}
    for i in range(len(arr)):
        arr[i] = dict.get(arr[i])
    return ''.join(arr)


print(solution(23))
print(solution(51))
print(solution(100))

# dict 사용법 정리