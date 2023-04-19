import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

if __name__=="__main__":
    N = int(sys.stdin.readline())
    dist = [[-1] * (N+1) for _ in range(N+1)]
    queue = deque()
    queue.append([1, 0])
    dist[1][0] = 0
    answer = 2147000000
    while queue:
        s, c = queue.popleft()
        if dist[s][s] == -1:
            dist[s][s] = dist[s][c] + 1
            queue.append([s, s])
        if s+c <= N and dist[s+c][c] == -1:
            dist[s+c][c] = dist[s][c] + 1
            queue.append([s+c, c])
        if s-1 >= 0 and dist[s-1][c] == -1:
            dist[s-1][c] = dist[s][c] + 1
            queue.append([s-1, c])

    for i in range(N+1):
        if dist[N][i] != -1 and answer > dist[N][i]:
            answer = dist[N][i]
    print(answer)