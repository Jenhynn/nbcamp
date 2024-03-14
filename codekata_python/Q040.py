# 숨어있는 숫자의 덧셈
# my_string 안의 모든 자연수들의 합 return


def solution(my_string):
    integers = []
    elements = list(my_string)
    nums = ['1','2','3','4','5','6','7','8','9']
    for i in range(len(elements)):
        if elements[i] in nums:
            integers.append(elements[i])
        else:
            continue
    sums = sum(list(map(int, integers)))
    return sums


# 다른 사람 풀이 참고:
def solution2(my_string):
    answer = 0
    for i in my_string:
        try:
            answer = answer + int(i) #int일 경우에만 더한다
        except:
            pass #str 일 경우 pass됨 *****오늘의 TIL try, except 정리하기*****

    return answer

print(solution("aAb1B2cC34oOp"))
print(solution("1a2b3c4d123"))

print(solution2("aAb1B2cC34oOp"))
print(solution2("1a2b3c4d123"))