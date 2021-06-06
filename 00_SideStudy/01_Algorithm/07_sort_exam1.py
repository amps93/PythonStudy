#두 배열 A, B / 두 배열은 N개의 원소로 구성되어 있고 원소는 모두 자연수
#최대 K번 바꿔치기(A와 B의 원소 하나씩 서로 바꿈) 연산 수행
#최종 목표 : A의 모든 원소의 합이 최대가 되어야함
#배열 A의 모든 원소의 합의 최댓값을 출력하는 프로그램 작성

'''
예시)
n=5 k=3
a = [1,2,5,4,3]
b = [5,5,6,6,5]

코드 작성 후
a = [6,6,5,4,5]
b = [3,5,1,2,5]

출력결과
26
'''
'''
입력 조건
첫줄에 n,k가 공백으로 구분
둘째줄에 a의 원소가 공백으로 구분
셋째줄에 b의 원소가 공백으로 구분
'''
n, k = map(int,input('n과 k 입력 : ').split())
a = list(map(int, input('배열 a 입력 : ').split()))
b = list(map(int, input('배열 b 입력 : ').split()))

a.sort()
b.sort(reverse=True)

for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break
print(a)
print(sum(a))