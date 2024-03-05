#중복된 숫자 개수

def solution(array, n):
    list = []
    for i in array:
        if i == n:
            list.append(i)
        else:
            continue
    return len(list)

# print(solution([1,1,2,3,4,5],1))