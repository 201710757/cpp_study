from collections import deque
import numpy as np
def __solution(n, roads, sources, destination):
    answer = []

    cnt = 0
    _map = np.zeros([n+1, n+1])
    for [i, j] in roads:
        _map[i][j] = 1

    for source in sources:
        cnt = 0
        if source == destination:
            answer.append(cnt)
            continue

        route = [destination, source] if destination < source else [source, destination]
        if _map[route[0]][route[1]] == 1:
            answer.append(cnt+1)
            continue

        # print(_map)

        while True:
            # print(source, route)
            cnt += 1
            if route[0] > route[1]:
                answer.append(-1)
                break
            if _map[route[0]][route[1]] == 1:
                answer.append(cnt)
                break
            else:
                _flag = True
                # print("map : ", _map[route[0]])
                for idx, r in enumerate(_map[route[0]]):
                    if r == 1:
                        route[0] = idx
                        _map[route[0]][idx] = 0
                        _flag = False
                        break
                if _flag:
                    answer.append(-1)
                    break

    return answer

def _solution(n, roads, sources, destination):
    answer = []

    cnt = 0
    for source in sources:
        if source == destination:
            answer.append(cnt)
            continue
        
        route = [destination, source] if destination < source else [source, destination]
        
        while True:
            cnt += 1
            if route[0] > route[1]:
                answer.append(-1)
                break
            if route in roads:
                print(route, " / ", cnt)
                answer.append(cnt)
                break
            else:
                _flag = True
                for road in roads:
                    if road[0] == route[0]:
                        route[0] = road[1]
                        # cnt -= 1
                        _flag = False
                        break
                if _flag:
                    answer.append(-1)
                    break
        cnt = 0
    print("RES : ", answer)
    return answer


def ___solution(n, roads, sources, destination):
    answer = []

    _dict = {}
    for road in roads:
        try:
            _dict[str(road[0])].append([road[1], 0])
        except:
            _dict[str(road[0])] = [[road[1], 0]]

            '''
    for key in sorted(_dict.keys()):
        for idx, _ in _dict[key]:
            try:
                for n, cnt in _dict[str(idx)]:
                    _dict[key].append([n, cnt+1])
            except:
                pass
    '''

    for source in sources:
        route = [destination, source] if destination < source else [source, destination]
        if route[0] == route[1]:
            answer.append(0)
            continue
        try:
            for dest, cnt in _dict[str(route[0])]:
                if route[0] > dest:
                    break
                if dest == route[1]:
                    answer.append(cnt+1)
                    break
        except:
            answer.append(-1)
    return answer

def solution(n, roads, sources, destination):
    routes = []
    answer = []
    
    for source in sources:
        route = [destination, source] if destination < source else [source, destination]
        routes.append(route)
        
    for route in routes:
        if route[0] == route[1]:
            answer.append(0)
            continue
        


n = 5
roads = [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]]
sources = [1, 3, 5]
destination = 5

n, roads, sources, destination = 5, [[1, 2], [1, 4], [2, 4], [2, 5], [4, 5]], [1, 3, 5], 5#3, [[1, 2], [2, 3]], [2, 3], 1
print(solution(n, roads, sources, destination))