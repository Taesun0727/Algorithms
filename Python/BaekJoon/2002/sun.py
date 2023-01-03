import sys
from collections import deque

sys.stdin = open('../input.txt')

if __name__=="__main__":
    T = int(sys.stdin.readline())

    ent = {}
    exit = []

    for i in range(T):
        tmp = sys.stdin.readline().strip()
        ent[tmp] = i
    for _ in range(T):
        exit.append(sys.stdin.readline().strip())

    answer = 0

    for i in range(T-1):
        for j in range(i+1, T):
            if ent[exit[i]] > ent[exit[j]]:
                answer += 1
                break

    print(answer)
