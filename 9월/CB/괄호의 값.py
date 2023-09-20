s = input()

stack = []
for i in s:
    if i == '(' or i == '[':
        stack.append(i)
    else:
        if len(stack) < 1:
            stack.append('!!!')
            break
        if i == ')' and stack[-1] == '(':
            stack.pop()
        elif i == ']' and stack[-1] == '[':
            stack.pop()
            
if len(stack) != 0:
    print(0)

else:
    s = s.replace('()', '+2')
    s = s.replace('[]', '+3')
    s = s.replace('(', '+2*(')
    s = s.replace('[', '+3*(')
    s = s.replace(']', ')')

    print(eval(s))

