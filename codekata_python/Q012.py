#머쓱이보다 키 큰 사람

def solution(array, height):
    count =0
    for num in array:
        if num > height:
            count += 1
        else:
            continue
    return count


# print(solution([12,14,15,14,13,13,], 13))