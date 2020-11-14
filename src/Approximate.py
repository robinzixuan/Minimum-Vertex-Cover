from collections import deque, defaultdict 
import time
def Approximate(graph, vertices, cutoff_time):
    start_time = time.time()
    Cover = set()
    trace = []
    size = len(Cover)
    start = max(graph, key = lambda k: len(graph[k]))
    edges = set()
    Cover.add(start)
    for i in graph[start]:
        edges.add(str(start) +'-' + i)
    while time.time() - start_time < cutoff_time and len(Cover) > size:
        size = len(Cover)
        while edges:
            edge = edges.pop()
            v = edge.split('-')[1]
            key =  edge.split('-')[0]
            graph[int(v)].remove(key)
            graph[int(key)].remove(v)
        start = max(graph, key = lambda k: len(graph[k]))
        Cover.add(start)#
        if len(Cover) > size:
            trace.append(str(round(time.time() -start_time ,2)) + ' ' + str(len(Cover)))
        for i in graph[start]:
            edges.add(str(start) +'-' + str(i))
        #print(edges)
    return Cover, trace







