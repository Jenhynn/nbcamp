#배열 원소의 길이

def solution(strlist):
    count = []
    for i in strlist:
        length = len(i)
        count.append(length)
    return count

# print(solution(["We", "are", "the", "world!"]))