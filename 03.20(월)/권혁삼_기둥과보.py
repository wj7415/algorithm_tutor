def solution(n, build_frame):
    A = [[4] * (n + 2) for _ in range(n + 2)]
    B = [[4] * (n + 2) for _ in range(n + 2)]
    answer = []
    for com in build_frame:
        c, y = com[0], com[1]
        r = n - y
        a = com[2]
        b = com[3]
        # 벽면을 벗어나는 경우 제외
        if r < 0 or r >= n+1 or c < 0 or c >= n+1:
            continue
        # 보 바닥 제외
        if a == 1 and r == 5:
            continue
        # 기둥 삽입
        if b == 1 and a == 0:
            # 바닥 가능
            if r == 5:
                A[r][c] = 0
            else:
                # 위로 올라갈 기둥 위
                if A[r+1][c] == 0:
                    A[r][c] = 0
                # 보 끝 아래 좌우에 보가 없으면 (0,n 가능) / 아니면 무시
                elif (B[r][c-1]==1 and B[r][c]==4)or (B[r][c]==1 and B[r][c-1]==4):
                    A[r][c] = 0
        # 보 삽입
        elif b == 1 and a == 1:
            # 기둥 위 가능
            if A[r+1][c] == 0 or A[r+1][c+1]==0:
                B[r][c] = 1
            # 보 사이에 삽입(양 쪽에 보가 있어야 가능)
            elif B[r][c-1] == 1 and B[r][c+1] == 1:
                B[r][c] = 2
        # 기둥 삭제
        elif b == 0 and a == 0:
            # 기둥 조건
            if A[r-1][c] == 0:
                continue
            #보 끝이 걸린 조건이면 제거 불가
            if (B[r-1][c-1]==1 and (B[r-1][c]==4 or B[r-1][c-2]==4)) or (B[r-1][c]==1 and (B[r-1][c-1]==4 or B[r-1][c+1]==4)):
                continue
            if A[r][c]==0:
                A[r][c] = 4
        # 보 삭제
        elif b == 0 and a == 1:
            # 위에 기둥이 있으면 불가
            if A[r][c]==0 or A[r][c+1]==0:
                continue
            # 아래 기둥 없이 보 연결 시 불가 (사이일 경우 b=2)
            
            if B[r][c] == 1:
                B[r][c] = 4
    # print(A)
    for i in range(n+1):
            for j in range(n+1):
                if A[i][j] == 0 :
                    a = [j, n-i, A[i][j]]
                    answer.append(a)
                    
    for i in range(n+1):
            for j in range(n+1):
                if B[i][j] == 1:
                    b = [j, n-i, B[i][j]]
                    answer.append(b)
                    
    for i in range(n+1):
            for j in range(n+1):
                if B[i][j] == 2:
                    b = [j, n-i, B[i][j]-1]
                    answer.append(b)
    # print(A)
    answer.sort()
    return answer
