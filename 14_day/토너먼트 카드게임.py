import sys
sys.stdin = open("토너먼트_카드게임_input.txt")
def partition(a,l,r):
    if l == r:
        return l
    else:
        pivot = (l+r)//2
        left = partition(a,l,pivot)
        right = partition(a,pivot+1, r)

        if (data[left] == 1 and data[right] == 2) or (data[left] == 2 and data[right] == 3) or (data[left] == 3 and data[right] == 1):
            return right
        else:
            return left

T = int(input())

for tc in range(T):
    N = int(input())
    data = list(map(int, input().split()))
    # print(data)
    winner = partition(data,0,len(data)-1)+1
    print("#{} {}".format(tc+1, winner))