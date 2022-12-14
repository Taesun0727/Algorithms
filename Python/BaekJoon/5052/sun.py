import sys
from collections import deque

sys.stdin = open('../input.txt')

if __name__=="__main__":

    T = int(sys.stdin.readline())

    for k in range(T):
        N = int(sys.stdin.readline())
        phoneBook = []
        flag = True
        for _ in range(N):
            phoneBook.append(sys.stdin.readline().strip())

        phoneBook.sort()

        for i in range(N-1):
            if phoneBook[i] == phoneBook[i+1][:len(phoneBook[i])]:
                flag = False
                break
        if flag:
            print("YES")
        else:
            print("NO")

    A = sys.stdin.readline().strip()
    B = sys.stdin.readline().strip()
    dp = [0] * len(B)

    for i in range(len(A)):
        cnt = 0
        for j in range(len(B)):
            if cnt < dp[j]:
                cnt = dp[j]
            elif A[i] == B[j]:
                dp[j] = cnt + 1
    print(max(dp))

