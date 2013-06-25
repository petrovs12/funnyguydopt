#!/usr/bin/python
# -*- coding: utf-8 -*-
import lpsolve55
from lp_solve import *
from lp_maker import *
import math
import sys

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
    maxNumColors=math.floor(nodeCount//4)
    #overall number of variables= numNodes+numEdges
    c=([1]*maxNumColors)+([0]*(maxNumColors*nodeCount))
    lower=[0]*len(c)
    upper=[1]*len(c)
    intIndices=range(1,len(c)+1)
    b=[]
    e=[]
    #each node is colored with one color:
    A=[[0]*maxNumColors*(i+1)+[1]*maxNumColors+[0]*maxNumColors*(nodeCount-i-1) for i in range(nodeCount)]#total number of variabes=(maxnumcols)*(nodecount+1)
    b.append([1]*len(A))
    e.append([0]*len(A))#equality constraints
    # xik-yi<=0- that these are nodeCount*nodeCount constraints
    for nd in range(nodeCount):
        for col in range(maxNumColors):
            cons=[0]*len(c)
            cons[col]=-1
            cons[maxNumColors*(nd+1)+col]=1
            A.append(cons)
    e.append([-1]*(nodeCount*maxNumColors))
    b.append([0]*(nodeCount*maxNumColors))

    # the third constraind- one for each edge and each k
    #smaller than 1
    for ed in edges:
        for col in range(maxNumColors):
            cons=[0]*len(c)
            cons[(ed[0]+1)*maxNumColors+col]=1
            cons[(ed[1]+1)*maxNumColors+col]=1
            A.append(cons)
    e.append([-1]*(maxNumColors*edgeCount))
    b.append([1]*(maxNumColors*edgeCount))

    # #smaller than 1
    # for ed in edges:
    #     for col in range(nodeCount):
    #         cons=[0]*len(c)
    #         cons[ed[0]*(nodeCount+1)+col]=1
    #         cons[ed[1]*(nodeCount+1)+col]=1
    #         A.append(cons)
    # e.append([-1]*(nodeCount*edgeCount))
    # b.append([1]*(nodeCount*edgeCount))
    #
    # #larger than 0
    # for ed in edges:
    #     for col in range(nodeCount):
    #         cons=[0]*len(c)
    #         cons[ed[0]*(nodeCount+1)+col]=1
    #         cons[ed[1]*(nodeCount+1)+col]=1
    #         A.append(cons)
    # e.append([1]*(nodeCount*edgeCount))
    # b.append([0]*(nodeCount*edgeCount))

    #constraints 5 and 6 are in upper, lower and intIndices
    # a trivial greedy algorithm for filling the knapsack
    # it takes items in-order until the knapsack is full
    b = [val for subl in b for val in subl]
    e = [val for subl in e for val in subl]
    lp=lp_maker(c, A, b, e, lower, upper,intIndices,setminim=1)
    lpsolve('set_timeout',lp,20)
    lpsolve('solve', lp)
    obj=lpsolve('get_objective', lp)
    #print(c)
    #print(obj)
    x=lpsolve('get_variables', lp)[0]
    flag=lpsolve('get_variables', lp)[1]
    lpsolve('delete_lp', lp)
    # print(x)

    # for k in range(nodeCount):
    #     print(x[((k+1)*nodeCount):((k+2)*(nodeCount))])
    solution = [x[((node+1)*nodeCount):((node+2)*(nodeCount))].index(1)+1 for node in range(nodeCount)]
    sList=sorted(solution)
    sList.sort()
    d={}
    for i in sList:
        if(i in d.keys()):
            continue
        else:
            d[i]=len(d.keys())
    solution=map(lambda x:d[x],solution)
    objFunction=x
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

