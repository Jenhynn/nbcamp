# 순서쌍
# 순서를 정하여 짝지어 나타낸 쌍 (a,b)
# (a,b)의 곱이 자연수 n인 순서쌍의 개수 return


def solution(n):
    list = []
    for i in range(1, n+1):
        if n % i == 0:
            list.append(i)
        else:
            continue
    #return list
    return len(list)


print(solution(20))
print(solution(100))