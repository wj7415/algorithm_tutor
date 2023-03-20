def solution(n, build_frame):
    global answer
    answer = []
    for i in build_frame:
        x = i[0]
        y = i[1]
        a = i[2]
        b = i[3]
        if b == 1:
            build(x,y,a)
        elif b == 0:
            delete(x,y,a)
    answer.sort()
    return answer

#만들기 함수
def build(x,y,a):
    global answer
    if a == 0 and (y == 0 or ([x,y,1] in answer) or ([x-1,y,1] in answer) or ([x,y-1,0] in answer)):
        answer.append([x,y,a])
    elif a == 1 and (([x,y-1,0] in answer) or ([x+1,y-1,0] in answer) or (([x-1,y,1] in answer) and ([x+1,y,1] in answer))):
        answer.append([x,y,a])
    else:
        flag = False
#삭제 함수
def delete(x,y,a):
    global answer,flag,temp,answer1
    answer1 = answer.copy()                 #answer1으로 copy하여 삭제
    answer1.remove([x,y,a])
    flag = True
    temp = []
    for i in answer1:
        check(i[0],i[1],i[2])
    if flag:
        answer.remove([x,y,a])

#삭제 가능여부 확인함수(answer1에서 [x,y,a] 삭제 후 문제 조건에 맞게 구성이 되는지/ 단, check 함수에서는 순서에 영향이 없음으로 temp가 아닌 answer1에서 확인)
def check(x,y,a):
    global flag,temp, answer1
       if a == 0 and (y == 0 or ([x,y,1] in answer1) or ([x-1,y,1] in answer1) or ([x,y-1,0] in answer1)):
        temp.append([x,y,a])
    elif a == 1 and (([x,y-1,0] in answer1) or ([x+1,y-1,0] in answer1) or (([x-1,y,1] in answer1) and ([x+1,y,1] in answer1))):
        temp.append([x,y,a])
    else:
        flag = False  #조건에 따라 지을 수 없는 것이 있으면,flag를 False로 변경하여 삭제 못하게함.
