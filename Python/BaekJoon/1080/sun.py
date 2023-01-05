import sys
from collections import deque

sys.stdin = open('../input.txt')

def reverse(x, y):
    for i in range(x,x+3):
        for j in range(y, y+3):
            first_matrix[i][j] = 1 - first_matrix[i][j]

if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    first_matrix = [[0] * M for _ in range(N)]
    second_matrix = [[0] * M for _ in range(N)]
    count = 0
    flag = False

    for i in range(N):
        S = sys.stdin.readline().strip()
        for j in range(M):
            first_matrix[i][j] = int(S[j])
    for i in range(N):
        S = sys.stdin.readline().strip()
        for j in range(M):
            second_matrix[i][j] = int(S[j])

    for i in range(N-2):
        for j in range(M-2):
            if first_matrix[i][j] != second_matrix[i][j]:
                reverse(i, j)
                count += 1
            if first_matrix == second_matrix:
                break
        if first_matrix == second_matrix:
            break

    if first_matrix != second_matrix:
        print(-1)
    else:
        print(count)