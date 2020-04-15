import sys
sys.stdin = open('수열합치기_input.txt')

class Node:
    def __init__(self, d=0, p=None, n=None):
        self.data = d
        self.prev = p
        self.next = n

class Linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

def addList(lst, arr):
    first = last = Node(arr[0])
    for val in arr[1:]:
        new = Node(val, last)
        last.next = new
        last = new
    if lst.head is None:
        lst.head, lst.tail = first, last
    else:
        cur = lst.head
        while cur is not None:
            if cur.data > arr[0]: break
            cur = cur.next
        if cur is None: # 뒤에
            lst.tail.next = first
            first.prev = lst.tail
            lst.tail = last
        elif cur.prev is None: # 앞에
            lst.head.prev = last
            last.next = lst.head
            lst.head = first
        else:   # 중간
            first.prev = cur.prev
            cur.prev.next = first
            cur.prev = last
            last.next = cur
    lst.size += len(arr)

def printList(lst):
    if lst.head is None: return
    cur = lst.tail
    cnt = 0
    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.prev
        cnt += 1
        if cnt == 10: break
    print()

T = int(input())

for tc in range(1,T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    mylist = Linkedlist()
    for lst in arr:
        addList(mylist,lst)
    print("#{}".format(tc), end=" ")
    printList(mylist)
    print()