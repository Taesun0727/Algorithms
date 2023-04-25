import sys
from collections import deque
import copy
from heapq import heappush, heappop

sys.stdin = open('../input.txt')
delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def dfs(x1, y1, x2, y2, count):
    global result
    if count > result or count > 10:
        return
    if x1 == x2 and y1 == y2:
        return
    if (0 > x1 or N <= x1 or 0 > y1 or M <= y1) and (0 > x2 or N <= x2 or 0 > y2 or M <= y2):
        return
    if (0 > x1 or N <= x1 or 0 > y1 or M <= y1) or (0 > x2 or N <= x2 or 0 > y2 or M <= y2):
        result = min(result, count)
        return
    for i in range(4):
        dx1 = x1 + delta[i][0]
        dy1 = y1 + delta[i][1]
        dx2 = x2 + delta[i][0]
        dy2 = y2 + delta[i][1]
        if 0 <= dx1 < N and 0 <= dy1 < M and 0 <= dx2 < N and 0 <= dy2 < M:
            if board[dx1][dy1] != '#' and board[dx2][dy2] != '#' and (dx1, dy1, dx2, dy2) not in visited:
                visited.append((dx1, dy1, dx2, dy2))
                dfs(dx1, dy1, dx2, dy2, count + 1)
                visited.pop()
            elif board[dx1][dy1] == '#' and board[dx2][dy2] != '#' and (x1, y1, dx2, dy2) not in visited:
                visited.append((x1, y1, dx2, dy2))
                dfs(x1, y1, dx2, dy2, count + 1)
                visited.pop()
            elif board[dx1][dy1] != '#' and board[dx2][dy2] == '#' and (dx1, dy1, x2, y2) not in visited:
                visited.append((dx1, dy1, x2, y2))
                dfs(dx1, dy1, x2, y2, count + 1)
                visited.pop()
        else:
            visited.append((dx1, dy1, dx2, dy2))
            dfs(dx1, dy1, dx2, dy2, count + 1)
            visited.pop()

if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = []
    visited = []
    coin = []
    result = 11
    for _ in range(N):
        board.append(list(sys.stdin.readline().rstrip()))
    for i in range(N):
        for j in range(M):
            if board[i][j] == 'o':
                coin.append(i)
                coin.append(j)
                board[i][j] = '.'
    dfs(coin[0], coin[1], coin[2], coin[3], 0)
    if result == 11:
        print(-1)
    else:
        print(result)