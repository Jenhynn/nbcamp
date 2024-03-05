#배열 뒤집기

def solution(num_list):
    num_list.reverse()
    answer = num_list
    return answer

print(solution([1,2,3,4,5]))

#다른 풀이
def solution(num_list):
    answer = num_list[::-1]
    return answer

# print(solution([1,2,3,4,5]))