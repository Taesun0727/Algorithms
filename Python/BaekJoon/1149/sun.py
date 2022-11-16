import sys
sys.stdin = open('../input.txt')

if __name__=="__main__":
    N = int(sys.stdin.readline())
    board = []
    dp = [[0]* 3 for _ in range(N)]
    for _ in range(N):
        board.append(list(map(int, sys.stdin.readline().split())))
    dp[0] = board[0]

    for i in range(1, N):
        dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + board[i][0]
        dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + board[i][1]
        dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + board[i][2]
    print(min(dp[N-1]))