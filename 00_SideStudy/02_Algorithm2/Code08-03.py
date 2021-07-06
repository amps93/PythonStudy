class TreeNode():
    def __init__(self):
        self.left = None
        self.data = None
        self.right = None


memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '에이핑크', '걸스데이', '트와이스', '마마무'] #DB, Crawling row data

#첫번째 노드 생성
name = nameAry[0]

node = TreeNode()
node.data = name
memory.append(node)
root = node

for name in nameAry[1:]:
    node = TreeNode()
    node.data = name
    current = root
    while True:
        if name < current.data:
            if current.left == None:
                current.left = node
                break
            current = current.left
        else:
            if current.right == None:
                current.right = node
                break
            current = current.right


    memory.append(node)

print(memory)

###데이터 검색
findName = '임선비'
current = root
while True:
    if findName == current.data:
        print(findName,'을 찾았음')
        break
    elif findName < current.data:
        if current.left == None:
            print('없음')
            break
        current = current.left
    else:
        if current.right == None:
            print('없음')
            break
        current = current.right
