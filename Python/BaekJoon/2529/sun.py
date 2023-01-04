import sys
from collections import deque

sys.stdin = open('../input.txt')

answer = []
visited = [0] * 10
N = 0

def DFS(L):
    if L == N:
        return
    for i in range(10):
        if (not visited[i]):
            pass


if __name__=="__main__":
    T = int(sys.stdin.readline())
    S = list(sys.stdin.readline().split())
    N = len(S) + 1
