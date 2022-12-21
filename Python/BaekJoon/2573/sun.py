import sys
sys.stdin = open('../input.txt')

global N, M
delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]

def Melt_iceberg(iceberg):
    nextYearIceberg = [[0] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if (iceberg[i][j] != 0):
                for k in range(4):
                    dx = i + delta[i][0]
                    dy = j + delta[i][1]
                    if (dx >= 0 and dx < N and dy >= 0 and dy < M and iceberg[dx][dy] == 0):
                        nextYearIceberg[i][j] -= 1

    for i in range(N):
        for j in range(M):
            nextYearIceberg[i][j] += iceberg[i][j]

    return nextYearIceberg

def Counting_iceberg(iceberg):
    if (sum(iceberg) == 0):
        return 0




if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

