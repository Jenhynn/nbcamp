# n번째 원소까지
# num_list, num 주어질 때 num_list의 첫번째 원소부터 n번째 원소까지의 모든 원소를 담은 list를 return


def solution(num_list, num):
    answer = []
    for i in range(num):
        answer.append(num_list[i])
    return answer


print(solution([2,1,6],1))
print(solution([5,2,1,7,5],3))