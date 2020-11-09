def LS2(graph, time, seed, out_sol = False, out_trace = False):
    pass


'''
def readfile(filename):
    with open(filename, "r") as f:
        first_line = f.readline()
        num_vertrix = int(first_line.split(" ")[0])
        num_edge = int(first_line.split(" "
        )[1])
        opt = int(first_line.split(" ")[2])
        graph = defaultdict(list)
        index = 1
        for line in f:
            l = line.split(" ")
            for i in l:
                if i  !='\n':
                    graph[index].append(int(i))    
            index += 1 
    return graph
graph = readfile('../DATA/football.graph')
LS2(graph, 3, 5, out_sol = False, out_trace = False)
'''