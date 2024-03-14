# 카운트 업
# 정수 start_num과 end_num이 주어질 때 start_num부터 end_num까지의 숫자를 차례로 담은 리스트 return


def solution(start_num, end_num):
    answer = []
    for num in range(start_num, end_num+1):
        answer.append(num)
    return answer


print(solution(3,10))