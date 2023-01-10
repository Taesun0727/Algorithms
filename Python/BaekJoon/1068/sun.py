import sys
from collections import deque
from collections import defaultdict

sys.stdin = open('../input.txt')

def find(num):
    global answer
    for value in tree[num]:
        if value in tree:
            find(value)
        else:
            answer += 1

if __name__=="__main__":
    N = int(sys.stdin.readline())
    tree = defaultdict(list)
    arr = list(map(int, sys.stdin.readline().split()))
    delete_node = int(sys.stdin.readline())
    arr[delete_node] = -2147000000
    answer = 0

    for i in range(N):
        tree[arr[i]].append(i)

    find(-1)

    print(answer)