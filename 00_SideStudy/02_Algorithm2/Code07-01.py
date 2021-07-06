SIZE = 5
queue = [None for _ in range(SIZE)]

front = rear = -1

#삽입
rear += 1
queue[rear] = '화사'
rear += 1
queue[rear] = '솔라'
rear += 1
queue[rear] = '문별'

print(queue)

#추출(삭제)
front += 1
data = queue[front]
queue[front] = None
print(data)

front += 1
data = queue[front]
queue[front] = None
print(data)

front += 1
data = queue[front]
queue[front] = None
print(data)

print(queue)