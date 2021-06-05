# 리스트의 주요 메소드
# 리스트의 길이 계산 함수 : len()
a=[1,2,3,4,5,6,3,9,3]
print('리스트의 길이 %d '%len(a))

# 리스트의 요소
print(a.count(3))

# 리스트의 요소 추가, 삽입 : append(), insert()
a.append(100)
print(a)

a.append([110,120])
print(a)

a.insert(2,120) #2번째 위치에 120 삽입
print(a)

b=[]
b.append(5.5)
b.append(10)
b.append(6.5)
print(b)

# scores=[]
# for i in range(10):
#     score = int(input('점수 입력 : '))
#     scores.append(score)
# print(scores)

# 리스트의 요소 제거 : remove(), pop()
n = [1,2,3,4,5,3,4,-1,-5,10]
n.remove(3)
print(n)

data = n.pop(4) #n번째 값을 삭제 /아무것도 안쓰면 맨 뒤의 값 삭제
print(n)
print(data)

# 리스트의 확장 : extend()
a=[3,6,0,-4]
b=[40,30,20,50]
# a.append(b)
# a.insert(2,b)
# print(a)
# a.extend(b)

# 리스트의 요소를 정렬 : sort(), reverse()
a.sort()
a.sort(reverse=True)
print(a)

#reverse 함수 사용하지 않고 역정렬하기
for i in range(len(a)):
    # item=a.pop()
    # print(item)
    # b.append(a.pop())
    b.append(a.pop())
print(b)

#sorted함수
c=sorted(a)
print(c)

# 리스트의 요소 찾기 : index()
a = [3,6,0,4,-1]
b = a.index(3)
print(b)

# 리스트 요소 중 큰 갑, 작은 값 : min(), max()
a = [3,6,0,-4,1]
string = ['Grape','Apple','banana','melon']
print(max(a))
print(min(a))

print(max(string))
print(min(string))
