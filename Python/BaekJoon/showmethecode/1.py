import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

if __name__=="__main__":
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    dp = [[0,0] for _ in range(N)]
    answer = 0

    if arr[0] == 1:
        dp[0][0] = 1
        dp[0][1] = -1
    else:
        dp[0][0] = -1
        dp[0][1] = 1

    for i in range(1 ,N):
        if arr[i] == 1:
            dp[i][0] = max(1, dp[i-1][0]+1)
            dp[i][1] = max(-1, dp[i-1][1]-1)
        else:
            dp[i][0] = max(-1, dp[i-1][0]-1)
            dp[i][1] = max(1, dp[i-1][1]+1)
    for i in dp:
        answer = max(answer, max(i))

    print(answer)