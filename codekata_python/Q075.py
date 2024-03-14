# 배열 비교하기
# 두 배열의 길이가 다르면 배열의 길이가 긴 쪽이 더 크다
# 배열의 길이가 같다면 각 배열에 있는 모든 원소의 합을 비교하여 결과에 따름
# arr1, arr2에 대해 arr2 가 크면 -1, arr1이 크면 1, 두 배열 같으면 0


def solution(arr1, arr2):
    if len(arr1) != len(arr2):
        if len(arr1) > len(arr2):
            return 1
        else:
            return -1
    else:
        if sum(arr1) > sum(arr2):
            return 1
        elif sum(arr1) < sum(arr2):
            return -1
        else:
            return 0


print(solution([49, 13],[70, 11, 2]))
print(solution([100, 17, 84, 1], [55, 12, 65, 36]))
print(solution([1, 2, 3, 4, 5], [3, 3, 3, 3, 3]))