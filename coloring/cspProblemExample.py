__author__ = 'stefan'

from constraint import *
import itertools
def binary_search(gnodes=graphNodes,gedges=graphEdges, lo=2, hi=None):
    if hi is None:
        hi = len(graphEdges)
    prob=Problem()
    bestSoFar={'numNodes':hi,'assignment':{x:x for x in gnodes}}
    while lo < hi:
        mid = (lo+hi)//2
        prob.reset()
        prob.addVariables(graphNodes,range(mid))
        for i in graphEdges:
            prob.addConstraint(AllDifferentConstraint(),[i[0],i[1]])
        solutions   =prob.getSolution()
        if not solutions is None:
            bestSoFar['numNodes']=mid
            bestSoFar['assignment']=solutions
        if solutions is None:
            lo = mid+1
        else:
            hi = mid
    return bestSoFar

graphEdges=[ (0 ,16),
    (1, 2),
(1, 6),
(1, 7),
(1, 8),
(2, 11),
(2, 16),
(2, 17),
(3, 14),
(3, 16),
(3, 17),
(4, 7),
(4, 13),
(4, 17),
(5, 6),
(5, 11),
(6 ,18),
(9 ,12),
(10, 13),
(11, 17),
(13, 15),
(15 ,17),
(16 ,19)]
graphNodes=list(set(itertools.chain(*graphEdges)))
prob=Problem()
for i in graphEdges:
    prob.addConstraint(AllDifferentConstraint(),[i[0],i[1]])
constrStruct=prob._constraints
prob.addVariables(graphNodes,range(3))
solutions=prob.getSolution()
print(solutions)
#prob.addVariables(list(graphNodes),range(4))
prob.reset()
prob.addVariables(graphNodes,range(2))
for i in graphEdges:
    prob.addConstraint(AllDifferentConstraint(),[i[0],i[1]])
solutions=prob.getSolution()
print(solutions)

prob.reset()
prob.addVariables(graphNodes,range(3))
for i in graphEdges:
    prob.addConstraint(AllDifferentConstraint(),[i[0],i[1]])
solutions=prob.getSolution()

print(solutions)


print(binary_search())