#거스름돈 문제
n = 1260
count = 0

#큰 단위 화폐부터 차례대로 확인학
array = [500,100,50,10]

for coin in array:
    count += n // coin # 해당 화폐로 거슬러 줄 수 있는 동전의 개수 세기
    n %= coin

print(count)

#1이 될때까지 문제
n, k =map(int, input().split())

result = 0
while True:
    #N이 K로 나누어 떨어지는 수가 될 떄까지 빼기
    target = (n//k) * k
    result += (n-target)
    n = target
    #N이 K보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n<k:
        break
    #k로 나누기
    result += 1
    n //= k

#마지막으로 남은 수에 대하여 1씩 빼기
result += (n-1)
print(result)
'''
입력 예시
25 5
'''

#곱하기 혹은 더하기 문제
data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])

for i in range(1, len(data)):
    #두 수 중에서 하나라도 0 혹은 1인 경우 곱하기보다는 더하기 수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result += num
    else:
        result *= num

print(result)
'''
입력 예시1
02984
입력 예시1
567
'''

#모험가 길드 문제

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의 수

for i in data:#공포도를 낮은 것부터 하나씩 확인하며
    count += 1 #현재 그룹에 해당 모험가를 포함시키기
    if count >= i: #현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면 그룹 결성
        result += 1 #총 그룹의 수 증가시키기
        count = 0 #현재 그루에 포함된 모험가의, 수 초기화

print(result) #총 그룹의 수 출력

'''
입력 예시
5
2 3 1 2 2 
'''