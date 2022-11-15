import sys
sys.stdin = open('../input.txt')

if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    knowPeople = set(sys.stdin.readline().split()[1:])
    parties = []
    answer = 0
    for _ in range(M):
        tmp = list(sys.stdin.readline().split()[1:])
        parties.append(tmp)

    for _ in range(M):
        for party in parties:
            for human in party:
                if human in knowPeople:
                    knowPeople = knowPeople.union(party)

    for i in range(M):
        check = True
        for human in parties[i]:
            if human in knowPeople:
                check = False
                break
        if(check):
            answer += 1
    print(answer)