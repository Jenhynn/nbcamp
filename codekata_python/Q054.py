# n번째 원소부터
# 정수 리스트 num_list에서 n번째 원소부터 마지막 원소까지 모든 원소를 담은 리스트를 return


def solution(num_list, n):
    answer = num_list[n-1:]
    return answer


print(solution([2,1,6],3))
print(solution([5,2,1,7,5],2))