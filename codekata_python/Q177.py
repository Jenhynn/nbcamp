# 가까운 수
# 정수 배열 array, 정수 n. array에 들어있는 정수 중 n과 가장 가까운 수 return


# def solution(array, n):
#     distance = []
#     for i in range(len(array)):
#         distance.append(abs(n - array[i]))
#     sorted_d = sorted(distance)
#     if sorted_d[0] == sorted_d[1]:
#
#     for j in range(len(distance)):
#
#
#         if distance[j] == sorted_d[0]:
#             return array[j]
#
#
# print(solution([3, 10, 28], 20))
# print(solution([10, 11, 12], 13))


def solution(array, n):
    array.sort()
    distance = []
    for i in range(len(array)):
        distance.append(abs(n - array[i]))
    distance.sort()
    if n - distance[0] in array:
        return n - distance[0]
    elif n + distance[0] in array:
        return n + distance[0]


print(solution([3, 10, 28], 20))
print(solution([10, 11, 12], 13))