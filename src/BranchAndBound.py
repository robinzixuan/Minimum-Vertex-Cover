import time
import copy

def BranchAndBound(graph, vertices, cutoff_time, num_edge):
    start_time = time.time()
    Cover = set()
    UB = vertices
    trace = []
    Cover, traace = EMVC(graph, UB, Cover, trace, vertices, cutoff_time, num_edge)
    pass



def EMVC(graph, UB, C,trace, cutoff_time, num_edge):
    while time.time() - start_time < cutoff_time:
        if len(C) + DegLB(graph) >= len(UB):
            return vertices, traace
        if graph is empty:
            return Cover, traace
        v = max(graph, key = lambda k: len(graph[k])) 
        graph_copy = copy.deepcopy(graph)
        graph_copy_1 = copy.deepcopy(graph) 
        C_copy = copy.deepcopy(C)
        C_copy_1 = copy.deepcopy(C)
        del graph_copy_1[v]
        del graph_copy[v]
        for key in graph:
            del graph_copy[key]
            C_copy.add(key)
        C1, trace = EMVC(graph_copy, UB, C_copy,trace, cutoff_time, num_edge)
        C2, trace = EMVC(graph_copy_1, find_min(UB,C1), C_copy_1.add(v), trace, cutoff_time, num_edge)
        return find_min(C1,C2), trace
    return find_min(C1,C2), trace

        

def find_min(A,B):
    if len(A) <= len(B):
        return A
    else:
        return B


def DegLB(G):
    total_degree = 0
    start = max(G, key = lambda k: len(G[k]))
    num_edge = 0
    for key, value in G:
        num_edge += len(value)
    count = 0
    while total_degree < num_edge:
        del G[start]
        start = max(G, key = lambda k: len(G[k]))
        total_degree += len(G[start])
        count += 1
    del G[start]
    start = max(G, key = lambda k: len(G[k]))
    num_edge = 0
    for key, value in G:
        num_edge += len(value)
    return int(count +  num_edge/len(G[start]))










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