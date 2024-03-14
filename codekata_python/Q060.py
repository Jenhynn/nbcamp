# 뒤에서 5등까지
# 정수로 이루어진 리스트 num_list 에서 가장 작은 5개의 수를 오름차순으로 담은 리스트 return


def solution(num_list):
    num_list.sort()
    return num_list[:5]


print(solution([12, 4, 15, 46, 38, 1, 14]))