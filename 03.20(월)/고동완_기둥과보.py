#부분 점수 19.2점

def solution(n, build_frame):
    global bar, beam
    bar = [[0 for i in range(n + 1)] for i in range(n + 1)]
    beam = [[0 for i in range( n +1)] for i in range( n +1)]
    ans=[]


    for x,y,a,b in build_frame:  #x,y 좌표, a 종류(0:기둥, 1:보) , b(0:삭제, 1:설치)
        # 2by 2의 경우의 수로 나누어 고려한다(1.기둥(설치,삭제), 2.beam(설치,삭체))

        if a==0 and b==1: #기둥이고 설치인 경우
            if y==0 or bar[x][y-1]==1 or (x>0 and beam[x-1][y]==1) or beam[x][y]==1: #설치 가능한 경우
                #바닥면   #아래에 기둥이 있는 경우  # beam이 왼쪽에 있는 경우 #beam가 그 자리에 있는 경우 ####주의!! 이해) beam은 그 좌표에서 오른쪽으로 설치된다..
                bar[x][y]=1 #설치가능하면 기둥을 1로 설치함
            continue #설치 불가능한 경우 pass

        elif a==0 and b==0:  #기둥이고 삭제하는 경우
            # if bar[x-1][y]== 1 or bar[x+1][y]== 1 or bar[x][y+1]== 0
            '''
            # 기둥을 삭제가능한 경우
            # >> 왼쪽에 기둥 있는 경우 , 오른쪽에 기둥 있는 경우 , bar가  위에 없는 경우, 경우의 수의 조건이 복잡하다..
            #     bar[x][y] = 0
            '''
            bar[x][y]=0 #일단 삭제한다
            if not (y==0 or bar[x][y-1]==1 and (x>0 and beam[x-1][y]==1) or beam[x][y]==1) and (beam[x-2][y]==1): #조건을 불만족하면 다시 생성
                bar[x][y]=1

        elif a==1 and b==1: #beam이고 설치인 경우
            if bar[x][y-1]==1 or (x<n and y>0 and bar[x+1][y-1]==1) or ( x>0 and beam[x-1][y]==1 and beam[x+1][y]==1):
                beam[x][y]=1
            continue  #설치 불가능한 경우 pass


        elif a==1 and b==0: #beam이고 삭제하는 경우
            beam[x][y] = 0
            if not (bar[x][y-1]==1 or (x<n-1 and y>0 and bar[x+1][y-1]==1) or ( x>0 and beam[x-1][y]==1) and beam[x+1][y]==1):
                beam[x][y]=1
            if (y>0 and bar[x][y-1]==0) and (x>0 and beam[x+1][y])==1 :  #게속 틀리던 부분
                beam[x][y]=1

    for x in range(n+1):
        for y in range(n+1):
            if bar[x][y]==1:
                ans.append([x,y,0])
            if beam[x][y]==1:
                ans.append([x,y,1])

    return ans

# def main():
#     n=int(input())
#     # build_frame=[[input()]] #???이중 list 받기
#     # build_frame = [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]
#     build_frame=[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
#     print(solution(n, build_frame))

# if __name__=='__main__':
#     main()
