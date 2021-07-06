##함수 선언부
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear+1)%SIZE == front:
        return True
    else:
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
    rear = (rear+1)%SIZE
    queue[rear] = data

def deQueue():
    global SIZE, queue, front, rear
    if isQueueEmpty():
        print('Queue is empty')
        return
    front = (front + 1) % SIZE
    data = queue[front]
    queue[front] = None
    return data

#전역 변수부
SIZE = 5
queue = [None for _ in range(SIZE)]

front = rear = 0



#메인 코드부
if __name__ == '__main__':
    select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")

    while select != 'X':
        if select == 'I':
            data = input('데이터를 입력하세요')
            enQueue(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'E':
            data = deQueue()
            print(data)
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        elif select == 'V':
            print("큐 상태 : ", queue)
            print("front : ", front, ", rear : ", rear)
        else:
            print('오류 발생')

        select = input("삽입(I)/추출(E)/확인(V)/종료(X) 중 하나를 선택 ==> ")
    print('프로그램 종료')