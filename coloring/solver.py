#!/usr/bin/python
# -*- coding: utf-8 -*-
import networkx as nx
import sys
from networkx.algorithms.approximation import maximum_independent_set
def solveIt(inputData):
    # Modify this code to run your optimization algorithm
    # parse the input
    lines = inputData.split('\n')

    firstLine = lines[0].split()
    nodeCount = int(firstLine[0])
    edgeCount = int(firstLine[1])

    edges = []
    for i in range(1, edgeCount + 1):
        line = lines[i]
        parts = line.split()
        edges.append((int(parts[0]), int(parts[1])))
    # build a trivial solution
    # every node has its own color
        #items = len(values)
        #define n constraints fir each possible color:
    g=nx.Graph()
    g.add_edges_from(edges)
    solution=[-1]*len(g.nodes())
    i=0
    while(len(g.nodes())>0):
        maxDegVert=g.degree().keys()[g.degree().values().index(max(g.degree().values()))]
        # print(maxDegVert)
        indSet=maximum_independent_set(g)
        # indSet=maximum(g,[maxDegVert])
        for node in indSet:
            g.remove_node(node)
            solution[node]=i
        i=i+1
    # print(solution)
    # prepare the solution in the specified output format
    outputData = str(i) + ' ' + str(0) + '\n'
    outputData += ' '.join(map(lambda x:str(int(x)), solution))
    return outputData



if __name__ == '__main__':
    if len(sys.argv) > 1:
        fileLocation = sys.argv[1].strip()
        inputDataFile = open(fileLocation, 'r')
        inputData = ''.join(inputDataFile.readlines())
        inputDataFile.close()
        print solveIt(inputData)
    else:
        print 'This test requires an input file.  Please select one from the data directory. (i.e. python solverCSP1.py ./data/gc_4_1)'

