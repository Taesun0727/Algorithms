import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

if __name__=="__main__":
    N = int(sys.stdin.readline())
    arr = list(map(int, sys.stdin.readline().split()))
    near = [[-1, 2147000000] for _ in range(N)]
    count = []
    stack = []
    for i in range(N):
        while len(stack) > 0 and stack[-1][0] <= arr[i]:
            stack.pop()
        count.append(len(stack))
        if len(stack) > 0:
            near[i] = [stack[-1][1], i-stack[-1][1]]
        stack.append([arr[i], i])


    stack = []

    for i in range(N-1, -1, -1):
        while len(stack) > 0 and stack[-1][0] <= arr[i]:
            stack.pop()
        count[i] += len(stack)
        if len(stack) > 0:
            if stack[-1][1] - i < near[i][1]:
                near[i][0] = stack[-1][1]
        stack.append([arr[i], i])

    for i in range(N):
        if count[i] > 0:
            print(count[i], near[i][0]+1)
        else:
            print(0)