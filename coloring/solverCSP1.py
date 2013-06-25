#!/usr/bin/python
# -*- coding: utf-8 -*-
import lpsolve55
from lp_solve import *
from lp_maker import *
import sys
import itertools
import datetime
from constraint import *
from datetime import timedelta
secondsToWait=100
def binary_search(gnodes,gedges, lo=2, hi=None):
    start_time = datetime.datetime.now()
    if hi is None:
        hi = len(gedges)
    prob=Problem()
    bestSoFar={'numNodes':hi,'assignment':{x:x for x in gnodes},'flag':0}
    hi=17
    lo=18
    while lo < hi:
        mid = (lo+hi)//2
        prob.reset()
        prob.addVariables(gnodes,range(mid))
        for i in gedges:
            prob.addConstraint(AllDifferentConstraint(),[i[0],i[1]])
        solutions = prob.getSolution()
        if not solutions is None:
            bestSoFar['numNodes']=mid
            bestSoFar['assignment']=solutions
        if solutions is None:
            lo = mid+1
            d=datetime.datetime.now()-start_time
            # print(d.total_seconds())
            if(d.total_seconds()>secondsToWait):
                return bestSoFar
        else:
            hi = mid
            d=(datetime.datetime.now()-start_time)
            # print(d.total_seconds()>secondsToWait)
            # print(d.total_seconds())
            if(d.total_seconds()>secondsToWait):
                return bestSoFar
    bestSoFar['flag']=1
    return bestSoFar


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
    graphNodes=list(set(itertools.chain(*edges)))
    results=binary_search(graphNodes,edges)
    obj=results['numNodes']
    solution=results['assignment'].values()
    print(solution)
    flag=results['flag']
    # prepare the solution in the specified output format
    outputData = str(int(obj)) + ' ' + str(int(flag)) + '\n'
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

