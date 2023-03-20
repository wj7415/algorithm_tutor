def solve(result):
    R, C = 0, 1
    for x, y, a in result:
        if a == R: # 기둥
            if y != 0 and (x, y-1, R) not in result and (x-1, y, C) not in result and (x, y, C) not in result:
                return True #바닥 위, 밑에 보가 있는 경우, 왼쪽 밑에 보가 있는 경우, 우측 밑에 보가 있는 경우
        else: # 보
            if (x, y-1, R) not in result and (x+1, y-1, R) not in result and not ((x-1, y, C) in result and (x+1, y, C) in result):
                return True #왼쪽 아래에 기둥이 있는 경우, 오른쪽 아래에 기둥이 있는 경우, 왼쪽에 보, 오른쪽에 보
    return False

def solution(n, build_frame):
    res= set()
    
    for x, y, a, build in build_frame: 
        temp = (x, y, a)
        if build:
            res.add(temp)
            if solve(res):
                res.remove(temp)
        elif temp in res:
            res.remove(temp)
            if solve(res):
                res.add(temp)
    answer = map(list, res)
    
    return sorted(answer, key = lambda x : (x[0], x[1], x[2]))
