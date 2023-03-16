import sys
readl = sys.stdin.readline

N = int(readl())
lst = [list(map(int,readl().split())) for _ in range(N)]

#섹션을 최대한 많이 나눠라

maxx =0
for i in lst:
    for l in i:
        maxx = max(maxx,l)

# def mapp(height):
#     maplst = [[0]*N for _ in range(N)]

#     for r in range(N):
#         for c in range(N):
#             if lst[r][c] > height: #height 이상이면 잠기니까
#                 maplst[r][c] = 1
    
#     return maplst

def countsection(h):
    visited = [[False for _ in range(N)] for _ in range(N)]
    d = [(0,1),(1,0),(-1,0),(0,-1)]
    stack = []
    cnt = 0

    for i in range(N):
        for j in range(N):
            if lst[i][j] > h:
                if not visited[i][j]: 
                    stack.append((i,j))
                    visited[i][j] = True

                    while stack:
                        r,c = stack.pop()
                        for dr,dc in d:
                            nr = dr+r
                            nc = dc+c

                            if not 0<=nr<N : continue
                            if not 0<=nc<N : continue
                            if lst[nr][nc] <=h : continue
                            if visited[nr][nc]: continue

                            stack.append((nr,nc))
                            visited[nr][nc] = True

                    cnt += 1

    #print()
    return cnt




maxcnt = 1 # 아무데도 안잠기는 경우
for h in range(2,maxx+1):
    maxcnt = max(maxcnt, countsection(h))
#    print()
print(maxcnt)


