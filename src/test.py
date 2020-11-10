import argparse
import numpy
import time
from BranchAndBound import BranchAndBound
from Approximate import Approximate
from LocalSearch1 import LS1
from LocalSearch2 import LS2
import sys
import heapq
from collections import deque, defaultdict 


def readfile(args):
    if args.data:
        with args.data as f:
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
    else:
        raise FileNotFoundError('Please Inpyut data file')
    return graph






parser = argparse.ArgumentParser(description='Test Optimal Solution of MVC')
parser.add_argument('-inst', type=argparse.FileType('r'), help='Data for Test.', dest = 'data')
parser.add_argument('-alg', action='store', dest = 'alg', help='Alg Name')
parser.add_argument('-time', action='store', dest = 'time',type=int, help='cutoff time in second')
parser.add_argument('-seed', action="store", dest="seed", type=int, help='Random seed')
parser.add_argument('-out_sol', type=argparse.FileType('w'), dest = 'out_sol')
parser.add_argument('-out_trace', type=argparse.FileType('w'), dest = 'out_trace')
args = parser.parse_args()
graph = readfile(args)
if args.alg == 'BnB':
    sol, trace = BranchAndBound(graph,vertices, args.time, args.seed)
    if parser.out_sol and parser.out_trace:
        pass
    elif parser.out_sol:
        pass
    elif parser.out_trace:
        pass
    else:
        pass
elif args.alg == 'Approx':
    sol, trace = Approximate(graph, vertices, args.time, args.seed)
    if parser.out_sol and parser.out_trace:
        pass
    elif parser.out_sol:
        pass
    elif parser.out_trace:
        pass
    else:
        pass
elif args.alg == 'LS1':
    sol, trace = LS1_SA(graph, vertices, args.time, args.seed)
    if parser.out_sol and parser.out_trace:
        pass
    elif parser.out_sol:
        pass
    elif parser.out_trace:
        pass
    else:
        pass
elif args.alg == 'LS2':
    sol, trace = LS2_HC(graph, vertices, args.time, args.seed)
    if parser.out_sol and parser.out_trace:
        pass
    elif parser.out_sol:
        pass
    elif parser.out_trace:
        pass
    else:
        pass








