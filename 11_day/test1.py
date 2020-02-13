SIZE = 100
stack = [0] * SIZE
top = -1
def push(item):
    global top
    if top > SIZE -1 :
        return
    else:
        top += 1
        stack[top] = item

def pop():
    global top
    if top == -1:
        print("Stack is empty!")
        return 0
    else:
        result = stack[top]
        top -= 1

        return result

push(1)
push(2)
push(3)
item = pop()
print("pop item => %d " % item)
item = pop()
print("pop item => %d " % item)
item = pop()
print("pop item => %d " % item)

s = []
s.append(1)
s.append(2)
s.append(3)

if s:
    print(s.pop())
if s:
    print(s.pop())
if s:
    print(s.pop())
if s:
    print(s.pop())