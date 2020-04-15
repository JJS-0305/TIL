import sys
sys.stdin = open('암호_input.txt')

class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Linkedlist(object):
    def __init__(self):
        new_node = Node(None)
        self.front = new_node
        self.rear = new_node
        self.cnt = 0

    def insertLast(self, data):
        new_node = Node(data)
        if(self.cnt == 0):
            self.front = new_node
            self.rear = new_node
            self.cnt += 1
        else:
            self.rear.next = new_node
            self.rear = new_node
            new_node.next = self.front
            self.cnt += 1


    def insertAt(self, idx, N):

        current = self.front

        for _ in range(N):
            iter_i = 0
            while(iter_i < idx):
                previous = current
                current = current.next
                iter_i += 1

            if(iter_i == idx):
                data = previous.data + current.data
                new_node = Node(data)
                previous.next = new_node
                new_node.next = current
                current = new_node
                self.cnt += 1

    def printList(self):
        tmp = []
        current = self.front
        for i in range(self.cnt):
            tmp.append(current.data)
            current = current.next

        return tmp

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    numbers = Linkedlist()
    tmp = list(map(int, input().split()))
    for i in tmp:
        numbers.insertLast(i)
    numbers.insertAt(M, K)
    print("#{} {}".format(tc, ' '.join(map(str, numbers.printList()[:-11:-1]))))