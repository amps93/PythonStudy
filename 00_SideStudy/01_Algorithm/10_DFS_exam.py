#DFS 문제
#NxM 얼음틀, 구멍이 뚫려잇는 부분은 0 칸막이가 존재하는 부분은 1
#구멍이 뚫려있는 부분끼리 상하좌우로 붙어있는 경우 서로 연결되어 있는 것으로 간주
#얼음 틀의 모양이 주어졌을때 생성되는 총 아이스크림의 개수를 구하는 프로그램 작성

'''
입력 조건
1. 첫번째 줄에 N과M이 주어진다
2. 두번째 줄부터 N+1번째 줄까지 얼음틀의 형태가 주어진다
3. 구멍이 뚫려있으면 0 아니면 1

입력 예시
4 5
00110
00011
11111
00000
'''

#DFS로 특정 노드를 방문하고 연결된 모든 노드들도 방문
def dfs(x, y):
    #주어진 범위를 벗어나는 경우에는 즉시 종료
    if x<=-1 or x>=n or y<=-1 or y>=m:
        return False
    #현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        #상하좌우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

#N,M을 공백을 기준으로 구분하여 입력받기
n,m = map(int, input().split())

#2차원 리스트의 맵 정보 입력받기
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(n):
    for j in range(m):
    # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result += 1

print(result)