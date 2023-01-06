import sys
from collections import deque
from heapq import heappush, heappop
sys.stdin = open('../input.txt')

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]

def check():
    for i in range(R*H):
        for j in range(C):
            if board[i][j] == 0:
                return False
    return True

if __name__=="__main__":
    C, R, H = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(R*H)]
    visited = [[0] * C for _ in range(R*H)]
    delta2 = [[R, 0], [-R, 0]]
    answer = 0
    queue = deque()

    for i in range(R*H):
        for j in range(C):
            if board[i][j] == 1:
                queue.append((i, j))

    while(queue):
        tmp = queue.popleft()
        for i in range(4):
            dx = tmp[0] + delta[i][0]
            dy = tmp[1] + delta[i][1]
            if R * (tmp[0]//R) <= dx < R * (tmp[0]//R+1) and 0 <= dy < C and visited[dx][dy] == 0 and board[dx][dy] == 0:
                board[dx][dy] = 1
                visited[dx][dy] = visited[tmp[0]][tmp[1]] + 1
                answer = max(answer, visited[dx][dy])
                queue.append((dx, dy))
        for i in range(2):
            dx = tmp[0] + delta2[i][0]
            dy = tmp[1] + delta2[i][1]
            if 0 <= dx < R*H and 0 <= dy < C and visited[dx][dy] == 0 and board[dx][dy] == 0:
                board[dx][dy] = 1
                visited[dx][dy] = visited[tmp[0]][tmp[1]] + 1
                answer = max(answer, visited[dx][dy])
                queue.append((dx, dy))
    if not check():
        print(-1)
    else:
        print(answer)