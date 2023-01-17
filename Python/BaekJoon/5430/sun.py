import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

if __name__=="__main__":
    N = int(sys.stdin.readline())

    for _ in range(N):
        commands = sys.stdin.readline().strip()
        len_arr = int(sys.stdin.readline())
        s = sys.stdin.readline().rstrip()

        if s == "[]":
            arr = []
        else:
            arr = deque(list(s[1:-1].split(",")))
        flag = True
        reverse_count = 0

        for command in commands:
            if command == 'R':
                reverse_count += 1
            elif command == 'D':
                if len(arr) == 0:
                    flag = False
                    break
                else:
                    if reverse_count % 2 == 0:
                        arr.popleft()
                    else:
                        arr.pop()
        if (flag):
            if reverse_count % 2 == 1:
                arr.reverse()
            print("[" + ",".join(arr) + "]")
        else:
            print("error")