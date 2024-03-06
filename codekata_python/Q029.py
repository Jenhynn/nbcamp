#배열의 유사도

def solution(s1, s2):
    answer = 0
    if len(s1) >= len(s2):
        for i in range(len(s2)):
            if s2[i] in s1:
                answer += 1
            else:
                continue
    elif len(s1) < len(s2):
        for i in range(len(s1)):
            if s1[i] in s2:
                answer += 1
            else:
                continue
    return answer

print(solution(["a", "b", "c"],["com", "b", "d", "p", "c"]	))
print(solution(["n", "omg"], ["m","dot"]))

#교집합으로 푸는 방법

def solution2(s1,s2):
    return len(set(s1)&set(s2))

print(solution2(["a", "b", "c"],["com", "b", "d", "p", "c"]))
print(solution(["n", "omg"], ["m","dot"]))