import time
def BranchAndBound(graph, vertices, cutoff_time, seed, out_sol = False, out_trace = False):
    start_time = time.time()
    pass
    


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
BranchAndBound(graph,vertices, 3, 5, out_sol = False, out_trace = False)
'''