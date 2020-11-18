import time
import copy
import random
from collections import deque, defaultdict 
from queue import PriorityQueue
from collections import OrderedDict
from Approximate import Approximate
# import networkx as nx
# from networkx.algorithms.approximation import vertex_cover
'''
Acknowledgement:

This algorithm is based on the paper: "Two New Local Search Strategies for Minimum Vertex Cover"
by Shaowei Cai, Kaile Su, Abdul Sattar

Using the Algorithm 1: NuMVC
1 NuMVC (G,cutoff)
  Input: graph G = (V;E), the cutoff time
  Output: vertex cover of G
2 begin
3    initialize edge weights and dscores of vertices;
4    initialize the confChange array as an all-1 array;
5    construct C greedily until it is a vertex cover;
6    C := C;
7    while elapsed time < cutoff do
8       if there is no uncovered edge then
9           C := C;
10          remove a vertex with the highest dscore from C;
11          continue;
12      choose a vertex u 2 C with the highest dscore,
        breaking ties in favor of the oldest one;
13      C := Cnfug, confChange(u) := 0 and
        confChange(z) := 1 for each z 2 N(u);
14      choose an uncovered edge e randomly;
15      choose a vertex v 2 e such that
        confChange[v] = 1 with higher dscore, breaking
        ties in favor of the older one;
16      C := C [ fvg, confChange(z) := 1 for each
        z 2 N(v);
17      w(e) := w(e) + 1 for each uncovered edge e;
18      if w  
        then w(e) := b  w(e)c for each edge e;
19  return C;
'''
def removing(C, graph, vertices, confChange, dscores, edge_weights, uncovered_edges, u):
    # confChange(u) := 0
    confChange[u] = 0
    # confChange(z) := 1 for each z 2 N(u);
    dscores[u] *= -1
    for neighbor in graph[u]:
        neighbor = int(neighbor)
        if neighbor not in C:
            uncovered_edges.append((u, neighbor))
            uncovered_edges.append((neighbor, u))
            confChange[neighbor] = 1
            dscores[neighbor] += edge_weights[u][neighbor]
        else:
            dscores[neighbor] -= edge_weights[u][neighbor]
def adding(C, graph, vertices, confChange, dscores, edge_weights, uncovered_edges, vertex):
    # confChange(z) := 1 for each z 2 N(u);
        dscores[vertex] *= -1
        for neighbor in graph[vertex]:
            neighbor = int(neighbor)
            if neighbor not in C:
                uncovered_edges.remove((vertex, neighbor))
                uncovered_edges.remove((neighbor, vertex))
                confChange[neighbor] = 1
                dscores[neighbor] -= edge_weights[vertex][neighbor]
            else:
                dscores[neighbor] += edge_weights[vertex][neighbor]



def HillClimbing(graph, vertices, cutoff_time, seed, out_sol = False, out_trace = False):
    start_time = time.time()
    uncovered_edges = []
    trace = []
    graph_copy = copy.deepcopy(graph)

    # initialize edge weights and dscores of vertices
    edge_weights = {}
    for v in vertices:
        v = int(v)
        neighbors = graph[v]
        temp_dic = {}
        for neighbor in neighbors:
            temp_dic[int(neighbor)] = 1
        edge_weights[v] = temp_dic
    dscores = {}
    # initialize the confChange array as an all-1 array
    confChange = {}
    for v in vertices:
        dscores[int(v)] = 0
        confChange[int(v)] = 1
    # construct C greedily until it is a vertex cover
    timer = time.time()
    C, t = Approximate(graph_copy, vertices, cutoff_time)
    C = list(C)
    # C*=C
    C_solution = C.copy()
    # while elapsed time < cutoff do
    counter = 0
    # temp_length = 0
    while (time.time() - start_time < cutoff_time) and counter < 50000:
        # if there is no uncovered edge then
        while len(uncovered_edges) == 0:
            counter = 0
            C_solution = C.copy()
            # remove a vertex with the highest dscore from C
            max_temp = -float('inf')
            u = None
            for i in C:
                if dscores[i] > max_temp:
                    max_temp = dscores[i]
                    # choose a vertex u from C with the highest dscore
                    u = i
            # C := C\{u}
            # print(u)
            C.remove(u)
            trace.append(str(round(time.time() -start_time ,2)) + ' ' + str(len(C)))
            removing(C, graph, vertices, confChange, dscores, edge_weights, uncovered_edges, u)
<<<<<<< HEAD
            print (len(C))
        counter += 1
=======
            #print (len(C))
>>>>>>> 73a703230940c0755f9647c4406df0173844a570

        # breaking ties in favor of the oldest one;
        max_temp = -float('inf')
        u = None
        for i in C:
            if dscores[i] > max_temp:
                max_temp = dscores[i]
                # choose a vertex u from C with the highest dscore
                u = i
        # C := C\{u}
        C.remove(u)
        # trace.append(str(round(time.time() -start_time ,2)) + ' ' + str(len(C)))
        removing(C, graph, vertices, confChange, dscores, edge_weights, uncovered_edges, u)



        # choose an uncovered edge e randomly
        e = random.choice(uncovered_edges)
        # choose a vertex v 2 e such that confChange[v] = 1 with higher dscore
        vertex = None
        if dscores[e[0]] > dscores[e[1]]:
            vertex = e[0]
        else:
            vertex = e[1]
        # C := C'U'{v}
        C.append(vertex)
        adding(C, graph, vertices, confChange, dscores, edge_weights, uncovered_edges, vertex)
        
        # w(e) := w(e) + 1 for each uncovered edge e;
        for x in uncovered_edges:
            edge_weights[x[1]][x[0]] += 1
            dscores[x[0]] += 1
    return C, trace
    
 
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
     if '\n' in i:
                        i = i.replace('\n','')

graph, vertices, num_edge = readfile('../DATA/karate.graph')
print(graph)
HillClimbing(graph,vertices, 200, 5, out_sol = False, out_trace = False)
'''
