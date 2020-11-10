from collections import deque, defaultdict 
import time
def Approximate(graph, vertices, cutoff_time, seed):
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
            v = edge.split('-')[1]
            key =  edge.split('-')[0]
            best_path.append(str(round(time.time() -start_time ,2)) + ' ' + str(len(Cover)))
            graph[int(v)].remove(key)
            graph[int(key)].remove(v)
        start = max(graph, key = lambda k: len(graph[k]))
        Cover.add(start)#
        for i in graph[start]:
            edges.add(str(start) +'-' + str(i))
        #print(edges)
    return Cover, best_path





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
graph, vertices = readfile('../DATA/star.graph')
Cover, best_path = Approximate(graph,vertices,  10, 5)
print(len(Cover))
print(len(best_path))
'''


