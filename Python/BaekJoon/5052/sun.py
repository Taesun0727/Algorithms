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