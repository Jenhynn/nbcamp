#배열 두 배 만들기

def solution(numbers):
    answer = []
    for number in numbers:
        double = number * 2
        answer.append(double)
    return answer

print(solution([1, 2, 3, 4, 5]))
print(solution([1, 2, 100, -99, 1, 2, 3]))