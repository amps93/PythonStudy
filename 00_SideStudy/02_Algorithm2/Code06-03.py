def isStackFull():
    global SIZE, stack, top
    if top >= SIZE-1:
        return True
    else:
         return False

def push(data):
    global SIZE, stack, top
    if isStackFull():
        print('Stack is full')
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    if top == -1:
        return True

def pop():
    global SIZE, stack, top
    # 비었는지 확인
    if isStackEmpty():
        print('Stack is empty')
        return

    stack[top] = None
    top -= 1

SIZE = 5
stack = ['커피','녹차','꿀물','콜라',None]
top = 3

pop()
print(stack)
pop()
print(stack)
