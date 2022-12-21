import sys
from collections import deque

sys.stdin = open('../input.txt')

if __name__=="__main__":
    T = int(sys.stdin.readline())
    for _ in range(T):
        N, M = map(int, sys.stdin.readline().split())
        cost = [0] + list(map(int, sys.stdin.readline().split()))
        inDegree = [0] * (N+1)
        g = [[] for _ in range(N+1)]
        dp = [0] * (N+1)

        for i in range(M):
            a, b = map(int, sys.stdin.readline().split())
            g[a].append(b)
            inDegree[b] += 1

        end = int(sys.stdin.readline())
        q = deque()
        for i in range(1, N+1):
            if inDegree[i] == 0:
                q.append(i)
                dp[i] = cost[i];

        while(q):
            tmp = q.popleft()

            for i in g[tmp]:
                inDegree[i] -= 1
                dp[i] = max(dp[i], dp[tmp] + cost[i])
                if inDegree[i] == 0:
                    q.append(i)

        print(dp[end])
