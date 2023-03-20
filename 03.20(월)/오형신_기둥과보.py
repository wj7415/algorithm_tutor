
def val(res): # True : 설치 가능, False : 설치/해제 불가능
    for x, y, s in res: 
        if s == 0:  # 기둥이 성립하기 위한 3가지 조건 (s == 0)
            # 기둥은 바닥 위에 있거나 2) 보의 한쪽 끝 부분 위에 있거나 3) 다른 기둥 위에 있어야 합니다. 
            if y == 0 or (x-1,y,1) in res or ((x-1,y,1) in res and (x,y,1) in res) or (x,y-1,0) in res :
                return True 
            
        else: # 보가 설립하기 위한 2가지 조건 (S== 1)
            # 보는 한쪽 끝 부분이 기둥 위에 있거나, 양쪽 끝 부분이 다른 보와 동시에 연결되어 있어야 합니다.
            if ((x,y-1,0)) in res or ((x+1,y-1,0)) in res or ((x-1,y,1) in res and (x+1,y,1) in res) :
                return True 
            
           
def solution(n, build_frame):
    res = []  
    for x,y,s,b in build_frame: # data구성 (x좌표,y좌표,기둥/보,철거/설치)
        base = [x,y,s] # x좌표,y좌표,기둥/보
        
        if b == 1 : # 설치대상이면서 설치가능한 위치인경우 (True)
                res.append(list(base))
                if not val(res): 
                    #  print(list(base))
                     res.remove(list(base))
                     
        elif b == 0 : # 철거대상이면서 설치가능한 위치인 경우 (True)
                res.remove(list(base))  
                if not val(res): 
                     res.append(list(base))        
    
    # print(res)
    res = sorted(res,key = lambda x : (x[0],x[1],x[2])) # lambda sorted 정렬 0,1,2순서로 

    # return res
    print(res)
            

def main():
    n = int(input())
    build_frame = []
    # build_frame.append(list([1,0,0,1]))
    # build_frame.append(list([1,1,1,1]))
    # build_frame.append(list([2,1,0,1]))
    # build_frame.append(list([2,2,1,1]))
    # build_frame.append(list([5,0,0,1]))
    # build_frame.append(list([5,1,0,1]))
    # build_frame.append(list([4,2,1,1]))
    # build_frame.append(list([3,2,1,1]))

    build_frame.append(list([0,0,0,1]))
    build_frame.append(list([2,0,0,1]))
    build_frame.append(list([4,0,0,1]))
    build_frame.append(list([0,1,1,1]))
    build_frame.append(list([1,1,1,1]))
    build_frame.append(list([2,1,1,1]))
    build_frame.append(list([3,1,1,1]))
    build_frame.append(list([2,0,0,0]))
    build_frame.append(list([1,1,1,0]))
    build_frame.append(list([2,2,0,1]))

    # print(build_frame)

    solution(n,build_frame)
 
main()      
