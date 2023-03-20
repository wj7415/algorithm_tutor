def solution(n, build_frame):
    global area
    area=[[[None]] * (n+1) for row in range(n+1)]
    
    def construct(x, y, a, b):
        global area
        # print(f"x:{x} y:{y} building: {a} install : {b}")
        # print('construct')
        if area[n - y][x] == [None] and b == 1 and a == 0:
            area[n - y][x] = ["│"]

        elif area[n - y][x] == [None] and b == 1 and a == 1:
            area[n - y][x] = ["─"]

        elif area[n - y][x] == ["─"] and b == 1 and a == 0:
            area[n - y][x] = ["└ "]

        elif area[n - y][x] == ["│"] and b == 1 and a == 1:
            area[n - y][x] = ["└ "]





    def destruction(x, y, a, b):
        global area
        # print(f"x:{x} y:{y} building: {a} install : {b}")
        # print('desctruct')
        if area[n - y][x] == ["│"] and b == 0 and a == 0:
            area[n - y][x] = [None]

        elif area[n - y][x] == ["─"] and b == 0 and a == 1:
            area[n - y][x] = [None]

        elif area[n - y][x] == ["└ "] and b == 0 and a == 0:
            area[n - y][x] = ["─"]

        elif area[n - y][x] == ["└ "] and b == 0 and a == 1:
            area[n - y][x] = ["│"]



    def build_vali():
        global area
        vali=0
        for i in range(n+1):
            for j in range(n+1):
                if area[i][j] != [None]:
                    vali+=1
        # print(f'vali_start:{vali}')
        for i in range(n+1):
            for j in range(n+1):

                if area[i][j] != [None]:
                        if i == n and area[i][j] == ["─"]:
                            vali-=1; #print('vali basecase')

                        elif i == n and area[i][j] == ["│"]:
                            vali -= 1; #print('vali basecase')

                        elif area[i][j] == ["│"] :
                            if (0 <= (i+1) <= n+1) and area[i+1][j] == ["│"] :
                                vali -=1 ; #print('vali case1')
                            elif (0 <= (i+1) <= n+1) and area[i][j] == ["─"]:
                                vali -= 1; #print('vali case2')
                            elif (0 <= (i+1) <= n+1) and (0 <= (j-1) <= n+1) and area[i][j-1] == ["─"]:
                                vali -= 1; #print('vali case3')

                        elif area[i][j] == ["─"] :
                            if (i+1 <= n+1) and area[i+1][j] ==["│"]:
                                vali -= 1; #print('vali case4')
                            elif (i+1 <= n+1) and (0 <= j-1 ) and area[i+1][j+1] ==["│"]:
                                vali -= 1; #print('vali case5')
                            elif (0 <= j-1 ) and (j+1 <= n+1) and area[i][j-1] == ["─"] and area[i][j+1] == ["─"]:
                                vali -= 1; #print('vali case6')

        # print(f'vali_fianl:{vali}')

        if vali == 0:
            # print('pass validation')
            return True
        else:
            # print('validated')
            return False

    def export():
        global area
        result_list=[]
        for i in range(n+1):
            for j in range(n+1):
                if area[i][j] == ["─"]:
                    result_list.append([j,n-i,1])
                elif area[i][j] == ["│"]:
                    result_list.append([j,n-i, 0])
                elif area[i][j] == ["└"]:
                    result_list.append([j,n-i, 1]) ; result_list.append([j,n-i, 0])
        result_list.sort()
        return result_list



    for i in build_frame:
        x,y,a,b = i
        if b == 1:
            construct(x, y, a, 1)
            if build_vali() == False:
                destruction(x, y, a, 0)
        if b == 0:
            destruction(x, y, a, 0)
            # areaprint();
            # print()
            if build_vali() == False:
                construct(x, y, a, 1)

        # areaprint();print()

    answer = export()
    
    return answer
