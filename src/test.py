import argparse
import numpy
import time
from Graph import Graph, Vertex

parser = argparse.ArgumentParser(description='Test Optimal Solution of MVC')
parser.add_argument('-inst', type=argparse.FileType('r'), help='Data for Test.', dest = 'data')
parser.add_argument('-alg', action='store', dest = 'alg', help='Alg Name')
parser.add_argument('-time', action='store', dest = 'time',type=int, help='cutoff time in second')
parser.add_argument('-seed', action="store", dest="seed", type=int, help='Random seed')
parser.add_argument('-out_sol', type=argparse.FileType('w'), dest = 'out_sol')
parser.add_argument('-out_trace', type=argparse.FileType('w'), dest = 'out_trace')
args = parser.parse_args()



if args.data:
    with args.data as f:
        first_line = f.readline()
        num_vertrix = int(first_line.split(" ")[0])
        num_edge = int(first_line.split(" ")[1])
        opt = int(first_line.split(" ")[2])
        graph = Graph()
        '''
        for line in f:
            u = int(line.split(" ")[0])
            v = int(line.split(" ")[1])
            w = int(line.split(" ")[2])
            if u not in graph.get_vertices():
                graph.add_vertex(u)
            if v not in graph.get_vertices():
                graph.add_vertex(v)
            graph.add_edge(u,v, w)
        '''
else:
    raise FileNotFoundError('Please Inpyut data file')


if args.out_sol:
    pass

if args.out_trace:
    pass

