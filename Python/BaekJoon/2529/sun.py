import sys
from collections import deque

sys.stdin = open('../input.txt')

answer = []
visited = [0] * 10
N = 0

def check(num1, num2, op):
    if op == '>':
        if int(num1) > int(num2):
            return True
    if op == '<':
        if int(num1) < int(num2):
            return True
    return False

def DFS(L, num):
    if L == N:
        answer.append(num)
        return
    for i in range(10):
        if (not visited[i]):
            if L == 0 or check(num[L-1], str(i), S[L-1]):
                visited[i] = 1
                DFS(L+1, num+str(i))
                visited[i] = 0


if __name__=="__main__":
    T = int(sys.stdin.readline())
    S = list(sys.stdin.readline().split())
    N = len(S) + 1

    DFS(0, '')

    print(answer[-1])
    print(answer[0])