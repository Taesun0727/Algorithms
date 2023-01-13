import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

if __name__=="__main__":
    N, K = map(int, sys.stdin.readline().split())
    max_num = 100001
    DP = [2147000000] * (max_num)
    queue = deque()
    queue.append(N)
    DP[N] = 0
    while(queue):
        tmp = queue.popleft()

        if 0 <= tmp-1 < max_num and DP[tmp-1] > DP[tmp]+1:
            DP[tmp-1] = min(DP[tmp-1], DP[tmp]+1)
            queue.append(tmp-1)
        if 0 <= tmp+1 < max_num and DP[tmp+1] > DP[tmp]+1:
            DP[tmp+1] = DP[tmp]+1
            queue.append(tmp+1)
        if 0 <= tmp*2 < max_num and DP[tmp*2] > DP[tmp]:
            DP[tmp*2] = DP[tmp]
            queue.append(tmp*2)
        if tmp-1 == K or tmp*2 == K:
            print(DP[K])
            break
