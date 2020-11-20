import time
import random
import math
from queue import PriorityQueue

def LS1_SA(graph, vertices, num_edge, cutoff_time, seed):
    # SA
    # random.seed(seed)
    start_time = time.time()
    alpha = 0.95  # temp decrease rate
    T0 = 50  # initial temp
    T = T0
    L = 100 # number of steps without significant improvement (determine if restart)
    ST = 10  # maximum times for restart
    threshold = 1  # define significant improvement
    uncovered = set()  # record uncovered edges
    best_f = len(vertices)
    trace = [str(round(time.time() - start_time, 2)) + ' ' + str(best_f)] # trace file content
    best_f3 = float('inf')

    # Initial solution



    cover, trace = init_vc(graph, vertices, trace, start_time)
    size = int(len(cover)/2)

    f = objective(cover, uncovered)
    best_cover = cover.copy()
    best_f = f

    # v = random.sample(vertices, size)
    # for i in range(size):
    #     if int(v[i]) not in cover:
    #         cover.add(int(v[i]))

    # cover, uncovered = init_vc2(graph, vertices)
    # f = objective(cover, uncovered)
    # best_cover = cover.copy()
    # best_f = f

    # print(cover)
    # print(uncovered)
    # print(len(cover))
    # print(len(uncovered))

    # cover = set()
    # for i in vertices:
    #     cover.add(int(i))

    f = objective(cover, uncovered)
    best_f2 = f
    best_cover2 = cover.copy()


    loop = 0
    initial_f = best_f2
    while loop < L and (time.time() - start_time) < cutoff_time:
    # while (time.time() - start_time) < cutoff_time:
        loop = loop + 1
        # Pick a neighbor
        # Pick a vertex
        # p1 = len(cover)/len(vertices)
        # if random.uniform(0,1) < p1:
        #     u = random.sample(vertices, 1)
        #     u = int(u[0])
        # else:
        #     u = random.sample(cover, 1)
        #     u = u[0]

        u = random.sample(vertices, 1)
        u = int(u[0])


        # print('Before neighbor')
        # print(len(cover))
        # print(len(uncovered))
        if u in cover:
            cover.remove(u)
            for i in graph[u]:
                i = int(i)
                if i not in cover:
                    uncovered.add((u, i))
                    uncovered.add((i, u))
        else:
            cover.add(u)
            for i in graph[u]:
                i = int(i)
                if i not in cover:
                    uncovered.remove((u, i))
                    uncovered.remove((i, u))

        # print('after neighbor')
        # print(len(cover))
        # print(len(uncovered))
        # Admit?
        # Probability
        deg_u = len(graph[u])/num_edge
        f1 = objective(cover, uncovered)
        dE = max(0, f1 - f)
        # if u in cover:
        #     P = math.exp(-(dE * (1 - deg_u)) / T)
        # else:
        #     P = math.exp(-(dE * (1 + deg_u)) / T)

        if u in cover:
            P = math.exp(-(dE) / T)
        else:
            P = math.exp(-(dE) / T)

        T = T * alpha
        # print(T)
        # print(P)
        if random.uniform(0, 1) < P:  # admit

            f = f1
            # print(f)
        else:
            if u in cover:
                cover.remove(u)
                for i in graph[u]:
                    i = int(i)
                    if i not in cover:
                        uncovered.add((u, i))
                        uncovered.add((i, u))
            else:
                cover.add(u)
                for i in graph[u]:
                    i = int(i)
                    if i not in cover:
                        uncovered.remove((u, i))
                        uncovered.remove((i, u))

        if f < best_f2 and len(uncovered) == 0:
            best_f2 = f
            best_cover2 = cover.copy()
            if best_f2 < best_f:
                best_f = best_f2
                trace.append(str(round(time.time() - start_time, 2)) + ' ' + str(best_f))
                best_cover = best_cover2.copy()
            if threshold < (initial_f-best_f2):
                initial_f = best_f2
                loop = 0 # reset loop
                T = T0

    # print('using ', time.time()-start_time, ' sec')
    # print(best_f)
    return best_cover, trace


def objective(cover, uncovered):
    a = 1.0
    b = 2.0
    f = a*len(cover)+b*len(uncovered)
    return f

def init_vc(graph, vertices, trace, start_time):
    pq = PriorityQueue()
    for i in graph:
        pq.put((len(graph[i]), i))
    VC = []
    for i in range(len(graph)):
        index = pq.get()[1]
        neighbor = graph[index]
        VC.append((index, neighbor))
    # VC = VC[::-1] #in descending order
    # print(VC)
    uncovered_edges = []
    ret = list(vertices)
    # print(ret)
    for i in VC:
        overlapped = True
        for neighbor in i[1]:
            if neighbor not in ret:
                overlapped = False
        if overlapped:
            ret.remove(str(i[0]))
            trace.append(str(round(time.time() - start_time, 2)) + ' ' + str(len(ret)))
    temp = []
    for i in ret:
        temp.append(int(i))
    cover = set(temp)
    return cover, trace

def init_vc2(graph, vertices):
    # cover = set()
    c = set()
    uncovered = set()
    # edges = set()
    size = len(vertices)
    num = int(size)
    print(num)
    # v = max(graph, key=lambda k: len(graph[k]))
    # for i in graph[v]:
    #
    for i in vertices:
        c.add(int(i))
    # for i in range(num):
    #     v = max(graph, key=lambda k: len(graph[k]))
    #     cover.add(v)
    #     c.remove(v)

    cover = set(random.sample(c,num))

    for i in range(size):
        i = i+1
        if i not in cover:
            for j in graph[i]:
                if int(j) not in cover:
                    uncovered.add((i, int(j)))
    return cover, uncovered





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
sol, trace = LS1_SA(graph,vertices, 3, 5)
'''