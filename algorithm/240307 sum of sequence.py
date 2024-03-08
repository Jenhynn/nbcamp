# 부분 수열의 합
# N개 이상의 자연수, 최소 1개 이상의 수의 합이 K가 되는 경우의 수 구하기
# 첫째 줄 테스트케이스 수 T, 각 테스트 첫째 줄에는 N, K, 그 다음 줄에는 N개의 자연수 수열 A


t = int(input())
n, k = map(int, input().split())
row = list(map(int, input().split()))


def recursive_sum(n, k):
    if n == 1:
        return
    return recursive_sum(n - 1, k)

