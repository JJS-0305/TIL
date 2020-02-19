def push(data):
    if len(stack2) == 0:
        stack2.append(data)
    elif data == '(':
        stack2.append(data)
    elif data == ')':
        while True:
            if stack2[-1] == '(':
                stack2.pop()
                break
            stack.append(stack2.pop())
    else:
        while True:
            if len(stack2) == 0:
                stack2.append(data)
                break
            elif rank[data] > rank[stack2[-1]]:
                stack2.append(data)
                break
            else:
                stack.append(stack2.pop())
    # print(stack)
    # print(stack2)
    # print()

rank = {'(': 0, '+' : 1, '-' : 1, '*' : 2 , '/': 2, ')' : 0}

T = 10

for tc in range(T):
    N = int(input())
    data = input()

    stack = []
    stack2 = []
    for i in range(N):
        if data[i] not in rank:
            stack.append(data[i])
        else:
            push(data[i])
    while True:
        if len(stack2) != 0:
            stack.append(stack2.pop())
        else:
            break

    # print(stack)

    operation = '+*'
    while True:
        if len(stack) == 1:
            print("#{} {}".format(tc+1,stack[0]))
            break
        for i in range(len(stack)):
            if stack[i] == '+':
                stack[i] = int(stack[i-2]) + int(stack[i-1])
                stack.pop(i-1)
                stack.pop(i-2)
                break
            elif stack[i] == '-':
                stack[i] = int(stack[i - 2]) - int(stack[i - 1])
                stack.pop(i - 1)
                stack.pop(i - 2)
                break
            elif stack[i] == '/':
                stack[i] = int(stack[i - 2]) // int(stack[i - 1])
                stack.pop(i - 1)
                stack.pop(i - 2)
                break
            elif stack[i] == '*':
                stack[i] = int(stack[i - 2]) * int(stack[i - 1])
                stack.pop(i - 1)
                stack.pop(i - 2)
                break