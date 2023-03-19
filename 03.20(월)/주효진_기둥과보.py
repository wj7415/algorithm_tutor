def solution(n, build_frame):
    answer = []

    def A(arr):  # 리스트 내에 있다.
        result = True if arr in answer else False
        return result

    def B(arr):  # 리스트 내에 없다.
        result = False if arr in answer else True
        return result

    for x,y,a,b in build_frame:
        if b == 1: # 설치
            if a == 0: # 기둥일 때
                # 바닥이거나, 다른 기둥 위 이거나, 왼쪽으로 보가 있거나, 오른쪽으로 보가 있을 때
                if y == 0 or A([x,y-1,0]) or A([x-1,y,1]) or A([x,y,1]):
                    answer.append([x,y,a])  # 추가

            else: # 보일 때
                # 왼쪽에 기둥 위이거나, 오른쪽에 기둥 위이거나, 직전에 보가 있으면서 다음 위치에도 보가 있을 때
                if A([x,y-1,0]) or A([x+1,y-1,0]) or (A([x-1,y,1]) and A([x+1,y,1])):
                    answer.append([x,y,a])  # 추가

        elif b == 0 and [x,y,a] in answer:  # 삭제
            if a == 0 : # 기둥일 때
                # 나를 의지한 기둥(x,y+1)이 좌/우 보(x-1,y+1),(x,y+1)가 없을 때, 삭제안됨
                if A([x,y+1,0]) and (B([x-1,y+1,1]) and B([x,y+1,1])):
                    continue
                # 나를 의지한 왼쪽 보(x-1,y+1)가 기둥(x-1,y)이 없고, 오른 보(x,y+1) or 왼 보(x-2,y+1)가 없을 때,
                if A([x-1,y+1,1]) and B([x-1,y,0]) and (B([x,y+1,1]) or B([x-2,y+1,1])):
                    continue
                # 나를 의지한 오른쪽 보(x,y+1)가 기둥(x+1,y+1)이 없고, 오른 보(x+1,y+1)or 왼 보(x-1,y+1)가 없을 때,
                if A([x,y+1,1]) and B([x+1,y,0]) and (B([x+1,y+1,1]) or B([x-1,y+1,1])):
                    continue
                answer.remove([x,y,a])

                                 
            else : # 보일 때
                # 나를 의지한 왼쪽 기둥(x,y)이 아래 기둥(x,y-1)이나 왼보(x-1,y)가 없을 때
                if A([x,y,0]) and (B([x,y-1,0]) and B([x-1,y,1])):
                    continue
                # 나를 의지한 오른쪽 기둥(x+1, y)이 아래 기둥(x+1,y-1)이나 오른보(x+1,y)가 없을 때
                if A([x+1,y,0]) and (B([x+1,y-1,0]) and B([x+1,y,1])):
                    continue
                # 나를 의지한 왼쪽 보(x-1,y)가 좌(x-1,y-1) 기둥 또는 우(x,y-1) 기둥이 없을 때
                if A([x-1,y,1]) and B([x-1,y-1,0]) and B([x,y-1,0]):
                    continue
                # 나를 의지한 오른쪽 보(x+1,y)가 좌(x+1,y-1) 기둥 또는 우(x+2,y-1) 기둥이 없을 때
                if A([x+1,y,1]) and (B([x+1,y-1,0]) and B([x+2,y-1,0])):
                    continue
                answer.remove([x,y,a])

    answer.sort()
    return answer
