#선택 정렬 : 시간 복잡도 O(N^2)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(len(array)):
    min_index = i #가장 작은 원소의 인덱스
    for j in range(i+1, len(array)):
        if array[min_index]>array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스와프

print(array)

#삽입 정렬 : 시간 복잡도 O(N^2)
#최선의 경우 O(N) 시간 복잡도 (이미 모두 정렬되어있을 경우)
array = [7,5,9,0,3,1,6,2,4,8]

for i in range(1, len(array)):
    for j in range(i, 0 ,-1): #인덱스 i부터 1까지 1씩 감소하며 반복하는 문법
        if array[j] < array[j-1]: #한칸씩 왼쪽으로 이동
            array[j], array[j-1] = array[j-1], array[j]
        else: #자기보다 작은 데이터를 만나면 그자리에 멈춤
            break

print(array)