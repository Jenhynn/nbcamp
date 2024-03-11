#이진 탐색 Binary Search
#수 찾기

#
# n = int(input())
# nlist = list(map(int, input().split()))
# m = int(input())
# mlist = list(map(int, input().split()))
#
# print(n, nlist, m, mlist)

n = int(input())
nlist = list(map(int, input().split()))
m = int(input())
mlist = list(map(int, input().split()))

def findX():
    for i in range(m):
        if mlist[i] in nlist:
            return 1
        else:
            return 0
print(n, nlist, m, mlist)
print(findX())