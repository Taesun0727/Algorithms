import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

if __name__=="__main__":
    N = int(sys.stdin.readline())
    classes = []
    for _ in range(N):
        start, end = map(int, sys.stdin.readline().split())
        classes.append([start, end])

    classes.sort(key=lambda x: (x[0], x[1]))
    heap = []
    heappush(heap, classes[0][1])
    for i in range(1, N):
        if heap[0] > classes[i][0]:
            heappush(heap, classes[i][1])
        else:
            heappop(heap)
            heappush(heap, classes[i][1])
    print(len(heap))