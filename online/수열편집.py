import sys
sys.stdin = open('수열편집_input.txt')

class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None    # 첫 번째 노드
        self.tail = None    # 마지막 노드
        self.size = 0       # 노드의 수

def printList(lst):     # lst: LinkedList객체
    if lst.head is None: return

    cur = lst.head
    print(lst.size, '[', end=" ")

    while cur is not None:
        print(cur.data, end=" ")
        cur = cur.next
    print(']')

def insertLast(lst, new):       # new: 새로 추가할 노드 객체
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        lst.tail.next = new
        lst.tail = new

    lst.size += 1

def deleteLast(lst):
    if lst.head is None: return

    pre, cur = None, lst.head
    while cur.next is not None:
        pre = cur
        cur = cur.next

    if pre is None:
        lst.head = lst.tail = None

    pre.next = None
    lst.tail = pre
    lst.size -= 1

def insertFirst(lst, new):
    if lst.head is None:
        lst.head = lst.tail = new
    else:
        new.next = lst.head
        lst.head = new

    lst.size += 1

def deleteFirst(lst):
    if lst.head is None: return

    # 노드가 1개일 경우 주의
    lst.head = lst.head.next
    if lst.head is None:
        lst.tail = None

    lst.size -= 1

def insertAt(lst, idx, new):    # idx: 인덱스 값
    # 빈 리스트일 경우, idx == 0
    if lst.head is None or idx == 0:
        insertFirst(lst,new)
    # 마지막 추가하는 경우 idx >= lst.size
    elif idx >= lst.size:
        insertLast(lst, new)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next

        new.next = cur
        pre.next = new
        lst.size += 1

def deleteAt(lst, idx):
    if lst.head is None or idx == 0:
        deleteFirst(lst)
    elif idx >= lst.size:
        deleteLast(lst)
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next

        pre.next = cur.next
        lst.size -= 1

def printAt(lst, idx):
    if lst.head == None or idx > lst.size: return -1
    elif idx == lst.size:
        return lst.tail.data
    else:
        pre, cur = None, lst.head
        for _ in range(idx):
            pre = cur
            cur = cur.next
        return cur.data


T = int(input())

for tc in range(1, T+1):
    N, M, L = map(int, input().split())
    ls = list(map(int, input().split()))
    mylist = LinkedList()

    for i in range(N):
        insertLast(mylist,Node(ls[i]))
    for _ in range(M):
        change = list(map(str, input().split()))

        if change[0] == 'C':
            deleteAt(mylist, int(change[1]))
            insertAt(mylist, int(change[1]), Node(int(change[2])))
        elif change[0] == 'I':
            insertAt(mylist, int(change[1]), Node(int(change[2])))
        else:
            deleteAt(mylist, int(change[1]))

    print("#{} {}".format(tc, printAt(mylist,L)))
