import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

class human:
    def __init__(self, w, h, l, n):
        self.w = w
        self.h = h
        self.l = l
        self.n = n

    def __lt__(self, other):
        if self.w > other.w:
            return True
        elif self.w == other.w and self.h == other.h:
            return self.l < other.l
        elif self.w == other.w:
            return self.h > other.h
        else:
            return False


if __name__=="__main__":
    N, M, K = map(int, sys.stdin.readline().split())
    first_line = []
    line = list(deque() for _ in range(M))
    for i in range(N):
        tmp = list(map(int, sys.stdin.readline().split()))
        if i == K:
            type = 1
        else:
            type = 0
        if i < M:
            heappush(first_line, human(tmp[0], tmp[1], i % M, type))
        else:
            line[i % M].append(human(tmp[0], tmp[1], i % M, type))


    count = 0
    # while(first_line):
    #     tmp = heappop(first_line)
    #     print(tmp.w, tmp.h, tmp.l, tmp.n)

    while(first_line):
        tmp = heappop(first_line)
        if tmp.n == 1:
            break
        if len(line[tmp.l]) != 0:
            heappush(first_line, line[tmp.l].popleft())
        count += 1
    print(count)