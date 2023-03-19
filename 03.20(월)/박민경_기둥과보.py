

def solution(n, build_frame):
    answer = [[]]
    
    #기둥
    sero = [[-1 for _ in range(n)] for _ in range(n)]
    #보
    garo = [[-1 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        sero[i][0] = 0
    # -1 : 설치 불가
    #  0 : 설치 가능
    #  1 : 설치 
    # 위 설정으로는 삭제가 구현이 어려움,,
    
    for x, y, types, install in build_frame:
        if types == 0 #기둥 sero
            if install == 1: 
                if sero[x][y] == 0 or garo[x][y] == 1 or garo[x-1][y] == 1:
                    sero[x][y] = 1
                    #설치 가능 처리
                    garo[x][y+1] = 0
                    garo[x-1][y+1] = 0
                    sero[x][y+1] = 0
            else:
                if sero[x][y] == 1:
                    if sero[x][y+1] == 1 or garo[x][y+1] == 1:
                        continue
                    elif sero[x][y+1] == 2:
                        sero[x][y+1] = 1
                        sero[x][y] = 0
                    elif garo[x][y+1] == 2:
                        sero[x][y] = 0
                        garo[x][y+1] = 1
                    else:            
                        sero[x][y] = 0
                        
                     #todo
                        
        else:   #보 garo
            if install == 1:
                if garo[x][y] == 0 or sero[x+1][y-1] == 1:
                    garo[x][y] = 1
                    sero[x][y+1] = 0
            else:
                # todo
            
                    
        
    
    return answer
