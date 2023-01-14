import sys

sys.stdin = open('../input.txt')

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def DFS(x, y):
    board[x][y] = 1
    for i in range(4):
        dx = x + delta[i][0]
        dy = y + delta[i][1]
        if dx < 0:
            dx += N
        if dx == N:
            dx = 0
        if dy < 0:
            dy += M
        if dy == M:
            dy = 0
        if board[dx][dy] == 0:
            DFS(dx,dy)

if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int , sys.stdin.readline().split())) for _ in range(N)]
    count = 0

    for i in range(N):
        for j in range(M):
            if board[i][j] == 0:
                DFS(i,j)
                count += 1

    print(count)