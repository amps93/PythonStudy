#함수 선언부
def isQueueFull():
    global SIZE, queue, front, rear
    if rear != SIZE-1:
        return False
    elif rear == SIZE-1 and front == -1:
        return True
    else:
        for i in range(front+1, SIZE):
            queue[i-1] = queue[i]
            queue[i] = None
        front -= 1
        rear -= 1
        return False

def isQueueEmpty():
    global SIZE, queue, front, rear
    if front == rear:
        return True
    else:
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if isQueueFull():
        print('Queue is full')
        return
    rear += 1
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return
    front += 1
    data = queue[front]
    queue[front] = None
    return data

#전역변수부
SIZE = 5
queue = [None for _ in range(SIZE)]

front = rear = -1

#메인 코드부
# queue = ['화사', '솔라', '문별', '휘인', '선미']
# front = -1
# rear = 4

print('queue is full? -->', isQueueFull())
print('queue is empty? -->', isQueueEmpty())

enQueue('화사')
print(queue)
enQueue('솔라')
print(queue)
enQueue('문별')
print(queue)
enQueue('선미')
print(queue)
enQueue('휘인')
print(queue)

retData = deQueue()
print(retData)
retData = deQueue()
print(retData)


enQueue('재남')
print(queue)
enQueue('또재남')
print(queue)

