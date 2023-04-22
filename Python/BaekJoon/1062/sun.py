import sys
from collections import deque
from itertools import combinations

sys.stdin = open('../input.txt')

basic_alpha = {'a', 'n', 't', 'c', 'i'}
alpha = {ky: v for v, ky in enumerate(
        (set(map(chr, range(ord('a'), ord('z')+1))) - basic_alpha))}
input_chars = []

if __name__=="__main__":
    N, K = map(int, sys.stdin.readline().split())
    if K < 5:
        print(0)
    else:
        K -= 5
        result = 0
        for _ in range(N):
            tmp = 0
            for c in set(sys.stdin.readline().rstrip())-basic_alpha:
                tmp |= (1 << alpha[c])
            input_chars.append(tmp)
        power_by_2 = (2**i for i in range(21))
        for comb in combinations(power_by_2, K):
            test = sum(comb)

            count = 0
            for cb in input_chars:
                if test & cb == cb:
                    count += 1

            result = max(result, count)
        print(result)
