stack = [None for _ in range(5)]
top = -1

#push
top += 1
stack[top] = '커피'
top += 1
stack[top] = '녹차'
top += 1
stack[top] = '꿀물'
top += 1

print(stack)

#pop
top =2

data = stack[top]
stack[top] = None
top -= 1
print(data)

data = stack[top]
stack[top] = None
top -= 1
print(data)

data = stack[top]
stack[top] = None
top -= 1
print(data)