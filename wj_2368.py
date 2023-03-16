import sys
sys.setrecursionlimit(10**6)

read = sys.stdin.readline

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def dfs(r,c,j):
    global N, visited, a
    visited[r][c] = 1
    # print(r,c,j,'--------')
    # for i in range(N):
    #     print(visited[i])
    
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        #if 갈수없는곳에 대한 조건을 거는 것.
        if nr < 0 or nc < 0 or nr >= N or nc >= N or visited[nr][nc] == 1 or a[nr][nc] <= j:
            continue
        
        dfs(nr, nc, j)

def main():
    global N, visited, a
    
    N = int(read().rstrip())
    # visited = [[0 for _ in range(N)] for _ in range(N)]
    a = []
    cnt = 0
    max_cnt = 0
    
    for i in range(N):
        a.append(list(map(int, read().rstrip().split())))
    # print(a)
        
        
    for k in range(0,101):
        visited = [[0 for _ in range(N)] for _ in range(N)]   
        for i in range(N):
            for j in range(N):
                if visited[i][j] == 0 and a[i][j] > k:
                    # print('check1')
                    dfs(i,j,k)
                    cnt += 1
                    # print('cnt 수',cnt)
        # print(cnt)
                    
        max_cnt = max(max_cnt, cnt)
        # print('k',k,'--------')
        # for i in range(N):
        #     print(visited[i])
        # if k ==1:
            # break
        cnt = 0
        
        
        
    print(max_cnt)
    
if __name__ == "__main__":
    main()
