import sys

sys.stdin = open('../input.txt')

if __name__ == "__main__":
    N, M = map(int, sys.stdin.readline().split())

    cave = [0] * M

    for i in range(N):
        tmp = int(sys.stdin.readline())
        if i % 2 == 0:
            cave[M - tmp] += 1
        else:
            cave[0] += 1
            cave[tmp] -= 1
    print(cave)
    for i in  range(1, M):
        cave[i] += cave[i-1]

    print(cave)
    count = 0
    low = min(cave)
    for i in cave:
        if i == low:
            count += 1

    print(low, count)
