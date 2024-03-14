# 정수 찾기
# 정수 리스트 num_list, 찾으려는 정수 n
# num_list 안에 n 이 있으면 1, 없으면 0 return


def solution(num_list, n):
    if n in num_list:
        return 1
    elif n not in num_list:
        return 0


print(solution([1, 2, 3, 4, 5],3))
print(solution([15, 98, 23, 2, 15], 20))