'''
x: 설치 위치 x좌표(0<= x <= n)
y: 설치 위치 y좌표(0<= y <= n)
stuff: 구조물(보 1, 기둥 0)
operate: 작동(설치 1, 삭제 0)
'''

def possible(answer):

    #현재 가지고 있는 모든 건물을 체크해본다. 하나만 걸리면 이 함수는 False를 뱉고, 모두 괜찮으면 True를 반환
    #따라서 기저조건은 True 로 만들자

    for x, y, stuff in answer:
        # 설치된 것이 '기둥'인 경우
        if stuff == 0 : 
            # 설치할 수 있는 경우에 대해서 contiue
            # (1)기둥이 바닥에 잘 서있을때, (2)기둥 밑왼쪽에 보가 있을때 (3) 기둥 밑에 보가 있을때 (4) 기둥 밑에 기둥 있을때
            # 하기 조건문은 or 기준으로 분기를 각각 쳐도됨
            if y == 0 or [x-1,y,1] in answer or [x,y,1] in answer or [x,y-1,0] in answer:
                continue
            return False
        # 설치된 것이 '보'인 경우
        # 왜 else를 안쓸까? -> 명시적으로 분기를 쳐주는게 예외상황을 만들지 않음.
        elif stuff == 1: 
            #(1) 보 밑에 기둥이 있을때, (2) 보 오른쪽,아래에 기둥이 있을때 (3) 보 왼쪽, 오른쪽에 보가 있을때
            if [x,y-1,0] in answer or [x+1, y-1,0] in answer or ([x-1,y,1]) in answer and [x+1,y,1] in answer:
                continue
            return False
        
    #위 조건에도 False 분기로 하나도 빠지지 않았다. 그럼 지금 구조물은 성립! 안전진단 통과
    #기저 조건이 True인 이유는 한 구조물이라도 False이면 전체가 False이므로!! (99번 잘해도 1번 잘못하면 혼남)
    return True

def solution(n,build_frame):
    answer = []
    for frame in build_frame:
        x,y,stuff,operate = frame
        #삭제하는 경우
        if operate ==0: 
            answer.remove([x,y,stuff])
            #가능한 구조물인지 확인
            if not possible(answer):
                answer.append([x,y,stuff])
        #설치하는 경우
        if operate ==1:
            answer.append([x,y,stuff])
            #가능한 구조물인지 확인
            if not possible(answer):
                answer.remove([x,y,stuff])
    return sorted(answer)
