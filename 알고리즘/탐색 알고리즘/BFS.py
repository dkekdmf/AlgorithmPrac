graph = dict()

graph['A'] = ['B','C']
graph['B'] = ['A','D']
graph['C'] = ['A','G','H','I']
graph['D'] = ['B','E','F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C','J']
graph['J'] =['I']




def bfs(graph,startnode):
    ## 기본은 항상 두개의 리스트를 별도로 관리해주는 것
    
    need_visited,visited = list(),list()
    ## 시작노드 지정
    need_visited.append(startnode)
    ##만약 아직도 방문이 필요한 노드가 있다면
    while need_visited:
        ## 큐구조활용, pop(0)
        node = need_visited.pop(0)
        ##만약 그 노드가 방문한 목록에 없다면
        if node not in visited:
            ##방문한 목록에 추가하기
            visited.append(node)
            ##그 노드에 연결된 노드들
            need_visited.extend(graph[node])
    return visited

print(bfs(graph,'A'))
