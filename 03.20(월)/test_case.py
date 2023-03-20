from 임정_기둥과보 import *
import time

import numpy as np
def testcase():
    np.random.seed(1)
    # n = np.random.random_integers(5,100)  #좌표평면 범위 5<=  <=100
    n = 100 #극한으로 설정
    iter_n = np.random.random_integers(1,100)  
    build_frame = []
    for i in range(iter_n):
        x = np.random.random_integers(0,n) # x좌표 0<= <=n
        y = np.random.random_integers(0,n) # y좌표 0<= <=n
        a = np.random.choice([0,1])  #0은 기둥, 1은 보
        if i ==0:
            b = 0 
        else:
            b = np.random.choice([0,1])  #0은 설치, 1은 삭제(단, 삭제는 있는거 삭제해야함)
        if b == 1:
            get_ran = np.random.choice(i+1)
            x,y = build_frame[get_ran][:2]  # 만약 삭제라면 원래 있던 것에 build_frame 중 하나 선택해서 뽑고, x,y 할당 
        build_frame.append([x,y,a,b])
    result = solution(n,build_frame)
    # print(n,build_frame)
    return n,build_frame,result

def get_test():
    #기본 테스트 케이스 2개
    n_list = [5,5]
    build_frame_list = [[[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]],
                        [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]]
    result_list = [[[1,0,0],[1,1,1],[2,1,0],[2,2,1],[3,2,1],[4,2,1],[5,0,0],[5,1,0]],
                   [[0,0,0],[0,1,1],[1,1,1],[2,1,1],[3,1,1],[4,0,0]]]
    
    #임의 생성 테스트케이스 (극한)
    n,build_frame,result = testcase()
    n_list.append(n)
    build_frame_list.append(build_frame)
    result_list.append(result)


    start = time.time()
    for i in range(len(n_list)):
        print(i)
        if solution(n_list[i],build_frame_list[i]) == result_list[i]:
            print('pass',time.time() - start)
get_test()



