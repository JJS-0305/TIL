import sys
sys.stdin = open('베이비진_input.txt')

def chk_run(lst):
    for i in range(len(lst)-2):
        if lst.count(lst[i]+1):
            if lst.count(lst[i]+2):
                return True
    return False

def chk_triplet(lst):
    for i in range(len(lst)-2):
        if lst[i] == lst[i+1] == lst[i+2]:
            return True
    return False

T = int(input())

for tc in range(1,T+1):
    card = list(map(int, input().split()))
    player1 = []
    player2 = []
    for i in range(0,12,2):
        player1.append(card[i])
        player2.append(card[i+1])
        player1.sort()
        player2.sort()
        if i >= 4:
            if chk_run(player1) or chk_triplet(player1):
                print("#{} 1".format(tc))
                break
            elif chk_run(player2) or chk_triplet(player2):
                print("#{} 2".format(tc))
                break
    else: print("#{} {}".format(tc, 0))