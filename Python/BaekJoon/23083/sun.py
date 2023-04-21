import sys
sys.setrecursionlimit(300000)
from collections import deque
from heapq import heappush, heappop
sys.stdin = open('../input.txt')

def find_value(x, y):
    if x < 0 or y < 0 or x == N or y == M:
        return 0

    if board[x][y] == -1:
        value = 0

        value += find_value(x - 1, y)
        value += find_value(x, y - 1)

        if (y + 1) % 2 == 0:
            value += find_value(x + 1, y - 1)
        else:
            value += find_value(x - 1, y - 1)

        board[x][y] = int(value % X)

        return board[x][y]

    return board[x][y]

if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = list([-1] * M for _ in range(N))
    K = int(sys.stdin.readline())
    X = 1e9 + 7
    board[0][0] = 1

    for _ in range(K):
        R, C = map(int, sys.stdin.readline().split())
        board[R-1][C-1] = 0
    print(find_value(N-1, M-1))
