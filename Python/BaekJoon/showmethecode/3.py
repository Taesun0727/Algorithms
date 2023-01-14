import sys
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(10 ** 6)
sys.stdin = open('../input.txt')

def DFS(f, s, V, L):
    global answer
    if V + max_w * (C-L) <= answer:
        return
    answer = max(answer, V)
    for i in range(f+1, N):
        for j in range(s+1, M):
            DFS(i, j, V + W[A[i]-1][B[j]-1], L+1)

if __name__=="__main__":
    N, M ,C = map(int, sys.stdin.readline().split())
    W = [list(map(int, sys.stdin.readline().split())) for _ in range(C)]
    A = list(map(int, sys.stdin.readline().split()))
    B = list(map(int, sys.stdin.readline().split()))
    C = min(N, M)
    max_w = 0
    for value in W:
        max_w = max(max_w, max(value))
    answer = 0

    DFS(-1, -1, 0, 0)
    print(answer)