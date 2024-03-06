#짝수 홀수 개수

def solution(num_list):
    even_count = 0
    odd_count = 0
    for i in range(len(num_list)): #왜 len(num_list) - 1 이 아니지?
        if num_list[i] % 2 == 0:
            even_count += 1
        else:
            odd_count += 1
    answer = [even_count, odd_count]
    return len(num_list), answer

print(solution([1,2,3,4,5]))
print(solution([1,3,5,7]))