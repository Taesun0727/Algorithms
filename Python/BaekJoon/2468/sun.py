import sys
from collections import deque
from heapq import heappush, heappop
sys.setrecursionlimit(10**6)
sys.stdin = open('../input.txt')

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def DFS(x, y, board):
    board[x][y] = 0
    for i in range(4):
        dx = x + delta[i][0]
        dy = y + delta[i][1]
        if 0 <= dx < N and 0 <= dy < N and board[dx][dy] != 0:
            DFS(dx, dy, board)

def rainning(board):
    for i in range(N):
        for j in range(N):
            if board[i][j] > 0:
                board[i][j] -= 1
if __name__=="__main__":
    N = int(sys.stdin.readline())
    land = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    max_value = 0
    answer = 1

    for i in range(N):
        max_value = max(max_value, max(land[i]))

    for i in range(1, max_value):
        rainning(land)
        count = 0
        copy_land = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(N):
                copy_land[i][j] = land[i][j]

        for i in range(N):
            for j in range(N):
                if copy_land[i][j] > 0:
                    DFS(i,j,copy_land)
                    count += 1
        answer = max(answer, count)
    print(answer)