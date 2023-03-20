
answer = []
def solution(n, build_frame): # build_frame 좌표 입력 받고 결과 출력하기 위해서 리스트 생성
    
    for 좌표 in build_frame: # 입력 좌표 받은거 x,y : 좌표, a=(0기둥, 1보) b= (0삭제, 1설치)
        x, y, a, b = 좌표 #찍으면 리스트 형태로 받음
        if b == 1 : # 설치할 때 (0기둥 or 1보)
            if a == 0 : #기둥 설치
                if y == 0 : # 0층에서는 전부 설치가능
                    answer.append(좌표[:3])
                elif [x,y] in answer: # 1. 보의 끝부분 짓기, 현재위치가 1보 경우
                    answer.append(좌표[:3])
                elif [x,y-1,1] in answer: # 1. 보의 끝부분에 짓기
                    answer.append(좌표[:3])
                elif [x-1,y,0] in answer: # 2. 기둥위에 짓기
                    answer.append(좌표[:3])
                
            else : #보 설치 
                if [x,y-1,0] in answer: # 바로 전에 x 좌표에서 y-1에 0기둥이 있을 때 설치 가능
                    answer.append(좌표[:3])
                elif [x+1,y-1,0] in answer: # 바로 전에 x+1, y-1 좌표에서 0기둥이 있을 때 설치 가능
                    answer.append(좌표[:3])
                elif ([x-1,y,1] in answer) and ([x+1,y,1] in answer): # 양쪽 끝부분 보로 연결된 경우 설치 가능 
                    answer.append(좌표[:3])
        else : # b==0 일떄, 삭제 경우  ------------append 반대 ?, 답 갯수 줄어드니까 remove
            # pass
            # #else 부분에서 걸러내지 못하는 중임 -> 위에서 이상한것들 걸러짐
              #기둥
            if a == 0 : #기둥 삭제 경우  -> 
                if [x,y-1,0] in answer: #바로 아래 기둥 있을때
                    answer.remove(좌표[:3])
                elif [x-1,y,1] in answer: #바로 옆에 보가 있을때
                    answer.remove(좌표[:3])
                elif [x,y,1] in answer: #기둥있을떄
                    answer.remove(좌표[:3])
            else : # 보 삭제 경우
                if [x,y-1,1] in answer: #바로 전에 기둥 있을때
                    answer.remove(좌표[:3])
                elif [x+1,y-1,1] in answer: #다음에 받치고 있는 기둥 있을때
                    answer.remove(좌표[:3])
                elif ([x-1,y,0] and [x+1,y,0]) in answer: #양쪽 보사이 보 있을때 
                    answer.remove(좌표[:3])

    answer.sort()
    return answer

n = 5
build_frame = [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]
solution(5, build_frame)
print(answer)
