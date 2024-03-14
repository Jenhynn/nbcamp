#최댓값 만들기
import itertools

def solution(numbers):
    combinations = list(itertools.combinations(numbers, 2))
    max = 0
    for i in range(len(combinations)):
        multiple = combinations[i][0]*combinations[i][1]
        if max < multiple:
            max = multiple
        else:
            continue
    return max


print(solution([0, 31, 24, 10, 1, 9]))