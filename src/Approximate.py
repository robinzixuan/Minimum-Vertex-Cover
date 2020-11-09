from collections import deque, defaultdict 
import time
def Approximate(graph, vertices, cutoff_time, seed, out_sol = False, out_trace = False):
    start_time = time.time()
    Cover = set()
    best_path = []
    start = max(graph, key = lambda k: len(graph[k]))
    edges = set()
    Cover.add(start)
    for i in graph[start]:
        edges.add(str(start) +'-' + i)
    while time.time() - start_time < cutoff_time:
        while edges:
            edge = edges.pop()
            best_path.append(edge)
            v = edge.split('-')[1]
            key =  edge.split('-')[0]
            Cover.add(int(v))
            graph[int(v)].remove(key)
            graph[int(key)].remove(v)
        start = max(graph, key = lambda k: len(graph[k]))
        Cover.add(start)#
        for i in graph[start]:
            edges.add(str(start) +'-' + str(i))
        #print(edges)
    return Cover, best_path






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
graph, vertices = readfile('../DATA/star2.graph')
Cover, best_path = Approximate(graph,vertices,  3, 5, out_sol = False, out_trace = False)
print(Cover)
#print(best_path)