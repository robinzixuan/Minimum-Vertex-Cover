import time
import copy
from collections import deque, defaultdict 
from queue import PriorityQueue
from collections import OrderedDict 
import networkx as nx
from networkx.algorithms.approximation import vertex_cover


def HillClimbing(graph, vertices, cutoff_time, seed, out_sol = False, out_trace = False):

    #calculate the initial solution, the following code aims to improve this solution
    trace = []
    temp = init_vc(graph, vertices)
    vc_solution = []
    for i in temp:
        vc_solution.append(int(i))
    vc_solution = sorted(vc_solution)
    # print (vc_solution)

    #set up variables
    start_time = time.time()
    uncovered_edges = [] # empty means that "vertex cover is achieved"
    return_solution = copy.deepcopy(vc_solution)
    costs = [0]*(len(vertices) + 1)
    init_sol_length = len(vc_solution)

    #climbing
    while(time.time() - start_time < cutoff_time):

        #if reach a vertex cover
        while len(uncovered_edges) == 0:
            if len(return_solution) > len(vc_solution):
                return_solution = copy.deepcopy(vc_solution)
            # if min(costs) == 0:
            #     costs_index = 1
            # else:
            #     costs_index = costs.index(min(costs))
            # vc_solution.remove(costs_index)
            # costs, uncovered_edges = add_uc_edges(graph, vc_solution, costs, uncovered_edges, costs_index)
            temp_max = -1000000
            temp_node = None
            for node in vc_solution:
                if costs[int(node)] > temp_max:
                    temp_max = costs[int(node)]
                    temp_node = node
            vc_solution.remove(temp_node)
            costs, uncovered_edges = add_uc_edges(graph, vc_solution, costs, uncovered_edges, temp_node)

        #if not
        temp_max = -1000000
        temp_node = None
        for node in vc_solution:
            if costs[int(node)] > temp_max:
                temp_max = costs[int(node)]
                temp_node = node
        vc_solution.remove(temp_node)
        costs, uncovered_edges = add_uc_edges(graph, vc_solution, costs, uncovered_edges, temp_node)

        added = None
        if costs[int(uncovered_edges[0][0])] > costs[int(uncovered_edges[0][1])]:
            added = uncovered_edges[0][0]
        else:
            added = uncovered_edges[0][1]
        vc_solution.append(added)
        costs, uncovered_edges = rem_uc_edges(graph, vc_solution, costs, uncovered_edges, added)

        for i in uncovered_edges:
            costs[i[0]] += 1

    return vc_solution,trace

 
def add_uc_edges(graph, vc_solution, costs, uncovered_edges, costs_index):
    costs_index = int(costs_index)
    costs[costs_index] *= -1
    for vert in graph[costs_index]:
        if int(vert) not in vc_solution:
            uncovered_edges.append((costs_index, int(vert)))
            uncovered_edges.append((int(vert), costs_index))
            costs[int(vert)] += 1
        else:
            costs[int(vert)] -= 1
    return costs, uncovered_edges

def rem_uc_edges(graph, vc_solution, costs, uncovered_edges, costs_index):
    costs_index = int(costs_index)
    costs[costs_index] *= -1
    for vert in graph[costs_index]:
        if int(vert) not in vc_solution:
            # print (uncovered_edges)
            # print ((costs_index, int(vert)))
            uncovered_edges.remove((costs_index, int(vert)))
            uncovered_edges.remove((int(vert), costs_index))
            costs[int(vert)] -= 1
        else:
            costs[int(vert)] += 1
    return costs, uncovered_edges



# Heurestic solution found by iteration from max to min degree nodes and removing node if still vertex cover after
def init_vc(graph, vertices):
    vc_solution = []
    # sort the graph based on degree
    pq = PriorityQueue()
    for i in graph:
        pq.put((len(graph[i]), i))
    VC = []
    for i in range(len(graph)):
        index = pq.get()[1]
        neighbor = graph[index]
        VC.append((index, neighbor))
    VC = VC[::-1] #in descending order
    uncovered_edges = []
    ret = list(vertices)
    for i in VC:
        overlapped = True
        for neighbor in i[1]:
            if neighbor not in ret:
                overlapped = False
        if overlapped: ret.remove(str(i[0]))
    ret = sorted(ret)
    return ret






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
LS1(graph,vertices, 3, 5, out_sol = False, out_trace = False)
'''