import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

if __name__=="__main__":
    S = sys.stdin.readline().rstrip()
    stack = []

    for i in range(len(S)):
        if len(stack) == 0:
            stack.append(S[i])
            continue
        if len(stack) > 2:
            if "".join(stack[len(stack)-3:len(stack)]) == "PPA" and S[i] == "P":
                stack.pop()
                stack.pop()
                stack.pop()

        stack.append(S[i])


    if (len(stack) == 0 or (len(stack) == 1 and stack[0] == 'P')):
        print("PPAP")
    else:
        print("NP")