## 함수 선언 부분 ## 
def add_data(friend) :
	katok.append(None)
	klen = len(katok)
	katok[klen-1] = friend

def insert_data(position, friend) :
	katok.append(None)
	klen = len(katok)

	for i in range(klen-1, position, -1):
		katok[i] = katok[i-1]
		katok[i-1] = None

	katok[position] = friend

def delete_data(position) :
	klen = len(katok)
	katok[position] = None

	for i in range(position+1, klen, 1):
		katok[i-1] = katok[i]
		katok[i] = None

	del(katok[klen-1])

    

## 전역 변수 선언 부분 ## 
katok = []
select = -1	# 1: 추가, 2: 삽입, 3: 삭제, 4: 종료

## 메인 코드 부분 ## 

while select != 4:

	select = int(input("선택하세요(1: 추가, 2: 삽입, 3: 삭제, 4: 종료)--> "))

	if select == 1:
		name = input('이름 입력 -->')
		add_data(name)
		print(katok)
	elif select == 2:
		name = input('이름 입력 -->')
		num = int(input('번호 입력 -->'))
		insert_data(num,name)
		print(katok)
	elif select == 3:
		num = int(input('번호 입력 -->'))
		delete_data(num)
		print(katok)
	elif (select == 4):
		print(katok)
		exit
	else:
		print('1~4중 한 숫자를 입력하세요')
		continue




