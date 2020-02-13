def check_bracket(string):
    stack = []
    for ch in string:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if stack[-1] == "(":
                stack.pop()
            else: return False

    if len(stack) == 0:
        return True
    else: return False

str1 = '()()((()))'
print(check_bracket(str1))
str2 = '((()((((()((()())((())))))'
print(check_bracket(str2))