import sys
from collections import deque
import heapq

sys.stdin = open('../input.txt')

def dijkstra(start):
    dp[start] = 0
    heap = []
    heapq.heappush(heap, [0, start])

    while heap:
        w, cur  = heapq.heappop(heap)

        if dp[cur] < w:
            continue

        for dest, weight in graph[cur]:
            cost = dp[cur] + weight
            if dp[dest] > cost:
                dp[dest] = cost
                heapq.heappush(heap, [cost, dest])


if __name__=="__main__":
    Node = int(sys.stdin.readline())
    graph = [[] for _ in range(Node+1)]
    dp = [2147000000] * (Node+1)
    M = int(sys.stdin.readline())

    for _ in range(M):
        i, j, value = map(int, sys.stdin.readline().split())
        graph[i].append([j, value])

    start, end = map(int, sys.stdin.readline().split())

    dijkstra(start)
    print(dp[end])

