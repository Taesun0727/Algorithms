import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

if __name__=="__main__":
    N, D = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(10001)]
    for _ in range(N):
        start, end, express = map(int, sys.stdin.readline().split())
        arr[start].append([end, express])
    distance = [i for i in range(D+1)]

    for i in range(D+1):
        if i != 0:
            distance[i] = min(distance[i], distance[i-1]+1)
        for end, express in arr[i]:
            if end <= D and distance[end] > express + distance[i]:
                distance[end] = express + distance[i]

    print(distance[D])