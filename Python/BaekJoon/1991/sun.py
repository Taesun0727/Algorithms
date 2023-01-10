import sys
from collections import deque
from heapq import heappush, heappop

sys.stdin = open('../input.txt')

def preorder(root):
    if root != '.':
        print(root, end='')
        preorder(tree[root][0])
        preorder(tree[root][1])

def inorder(root):
    if root != '.':
        inorder(tree[root][0])
        print(root, end='')
        inorder(tree[root][1])

def postorder(root):
    if root != '.':
        postorder(tree[root][0])
        postorder(tree[root][1])
        print(root, end='')

if __name__=="__main__":
    N = int(sys.stdin.readline())
    tree = {}

    for i in range(N):
        root, left, right = sys.stdin.readline().strip().split()
        tree[root] = [left, right]

    preorder('A')
    print()
    inorder('A')
    print()
    postorder('A')