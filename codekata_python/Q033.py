# 중앙값 구하기
# 중앙값 = 순서대로 정렬했을 때 가장 중앙에 위치하는 값
# array의 중앙값을 return


def solution(array):
    sorted_array = sorted(array)
    mid = sorted_array[len(sorted_array)//2]
    return mid


print(solution([1,2,7,10,11]))
print(solution([9,-1,0]))
print(solution([-1,-2,0]))