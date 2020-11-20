import argparse
import numpy
import time
from BranchAndBound import BranchAndBound
from Approximate import Approximate
from LocalSearch1 import LS1_SA
from LocalSearch2 import HillClimbing
import sys
import heapq
import os
from collections import deque, defaultdict 
import multiprocessing as mp
import ThreadClass


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
                        if '\n' in i:
                            i = i.replace('\n','')
                        graph[index].append(i)   
                        vertices.add(i)
                index += 1 
    else:
        raise FileNotFoundError('Please Inpyut data file')
    return  graph,vertices, num_edge



def writefile(dicts, filename, sol, trace):
    sol_filename = dicts + filename +'.sol'
    trace_filename = dicts + filename +'.trace'
    with open(sol_filename,'w') as f:
        f.write(str(len(sol))+'\n')
        f.write(str(sol)[1:-1])
    f.close()
    with open(trace_filename,'w') as f:
        for i in trace:
            f.write(i + '\n')
    f.close()



parser = argparse.ArgumentParser(description='Test Optimal Solution of MVC')
parser.add_argument('-inst', type=argparse.FileType('r'), help='Data for Test.', dest = 'data')
parser.add_argument('-alg', action='store', dest = 'alg', help='Alg Name')
parser.add_argument('-time', action='store', dest = 'time',type=int, help='cutoff time in second')
parser.add_argument('-seed', action="store", dest="seed", type=int, help='Random seed')

args = parser.parse_args()
graph,vertices, number_edge  = readfile(args)

filename = args.data.name.split('/')[-1]
filename = filename.split('.')[0]
filename = filename  + '_' + args.alg + '_' + str(args.time)
dicts = os.getcwd()
if dicts.split('/')[-1] == 'src':
    dicts = '../Sol/'
else:
    dicts = dicts + '/Sol/'
if args.alg == 'BnB':
    sol, trace = BranchAndBound(graph,vertices, args.time, num_edge)
    writefile(dicts, filename, sol, trace)
elif args.alg == 'Approx':
    sol, trace = Approximate(graph, vertices, args.time)
    writefile(dicts, filename, sol, trace)
elif args.alg == 'LS1':
    filename +=  '_' + str(args.seed)
    sol, trace = LS1_SA(graph, vertices,num_edge, args.time, args.seed)
    writefile(dicts, filename, sol, trace)
elif args.alg == 'LS2':
    filename +=  '_' + str(args.seed)
    '''
    result = []
    for i in range(10):
        task = ThreadClass.MyThread(HillClimbing, (graph, vertices, args.time, args.seed))
        task.start()
        sol, trace = task.get_result()
        result.append(len(sol))

    print(result)
    '''
    sol, trace = HillClimbing(graph, vertices, args.time, args.seed)
    writefile(dicts, filename, sol, trace)
    








