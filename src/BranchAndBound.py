import time
import math
import sys


def BranchAndBound(graph, vertices, cutoff_time, num_edge):
    start_time = time.time()
    current_best = vertices
    uppper_bound = len(graph)
    trace = []

    # the large graph will lead recursion error: maximum recursion depth exceeded in comparison
    # so we need to set recursion limit
    if sys.getrecursionlimit() < uppper_bound:
        sys.setrecursionlimit(uppper_bound + 2)

    def backtracking(cover, cover_num, subgraph, subgraph_num_edge):
        if time.time() - start_time > cutoff_time:
            # timeout
            return

        nonlocal current_best, trace, uppper_bound
        # if there is no edge on current subgraph, there will search until status
        if subgraph_num_edge == 0:
            if len(cover) < uppper_bound:
                cost = time.time() - start_time
                current_best = [k for k, v in cover.items() if v]
                print(len(current_best), cost)
                uppper_bound = len(current_best)
                trace.append(str(cost) + ' ' + str(uppper_bound))
            return

        # vertex <- findHighestUncoveredDegree
        vertex, max_degree = findHighestUncoveredDegree(graph, cover)
        if max_degree is None:
            # all vertices selected
            return
        lb = math.ceil(subgraph_num_edge / max_degree)
        if cover_num + lb >= uppper_bound:
            # if current_used_vertex + lb >= current_best then pruning
            return

        # vertex is used
        cover[vertex] = True
        edges = subgraph[vertex]
        # remove the edge of the vertex
        for neighbor in edges:
            subgraph[neighbor].remove(vertex)
        del subgraph[vertex]

        # backtracking
        backtracking(cover, cover_num + 1, subgraph, subgraph_num_edge - len(edges))

        # vertex is unused
        # the vertex has been choosed, the vertex connected to that vertex has to be choosen
        # it not, the edge won't be covered
        new_cover = cover.copy()
        new_cover[vertex] = False
        for neighbor in edges:
            new_cover[neighbor] = True
        new_cover_num = len([k for k, v in new_cover.items() if v])
   
        # backtracking
        backtracking(new_cover, new_cover_num, subgraph, subgraph_num_edge - len(edges))

        # restore the edge of subgraph
        subgraph[vertex] = edges
        for neighbor in edges:
            subgraph[neighbor].add(vertex)
        del cover[vertex]

    # put the vertex connected to k into set so that we can modify on backtracking
    graph = {k: set([int(i) for i in v]) for k, v in graph.items()}
    backtracking({}, 0, graph, num_edge)
    return current_best, trace


def findHighestUncoveredDegree(graph, cover):
    '''
    find the maximum degree of vertex that has not been covered
    '''
    best_vertex, max_degree = None, None
    for k, v in graph.items():
        if k not in cover and len(v) > 0:
            if max_degree is None or max_degree < len(v):
                max_degree = len(v)
                best_vertex = k

    return best_vertex, max_degree


'''
def readfile(filename):
    with open(filename, "r") as f:
        first_line = f.readline()
        num_vertrix = int(first_line.split(" ")[0])
        num_edge = int(first_line.split(" ")[1])
        weight = int(first_line.split(" ")[2])
        graph = defaultdict(list)
        vertices = set()
        index = 1
        for line in f:
            l = line.split(" ")
            for i in l:
                if i  !='\n':
                    graph[index].append(i)   
                    vertices.add(i)
            index += 1 
    return graph,vertices
graph, vertices = readfile('../DATA/football.graph')
sol, trace = BranchAndBound(graph,vertices, 3)
'''
