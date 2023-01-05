import sys
from collections import deque

sys.stdin = open('../input.txt')

delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
board = []
R = 0
C = 0
answer = 0

def BFS(i, j):
    global answer
    check = [[2147000000] * C for _ in range(R)]
    check[i][j] = 0
    queue = deque()
    queue.append((i, j))

    while(queue):
        tmp = queue.popleft()
        for i in range(4):
            dx = tmp[0] + delta[i][0]
            dy = tmp[1] + delta[i][1]
            if 0 <= dx < R and 0 <= dy < C and check[dx][dy] == 2147000000 and board[dx][dy] == 'L':
                check[dx][dy] = check[tmp[0]][tmp[1]] + 1
                queue.append((dx, dy))

    max_value = 0
    for values in check:
        for value in values:
            if value != 2147000000:
                max_value = max(max_value, value)

    answer = max(answer, max_value)
if __name__=="__main__":
    R, C = map(int, sys.stdin.readline().split())

    for _ in range(R):
        S = sys.stdin.readline().strip()
        tmp = []
        for i in range(C):
            tmp.append(S[i])
        board.append(tmp)

    for i in range(R):
        for j in range(C):
            if board[i][j] == 'L':
                BFS(i, j)

    print(answer)