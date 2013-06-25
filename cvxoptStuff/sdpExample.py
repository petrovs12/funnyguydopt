__author__ = 'stefan'
import itertools
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

from cvxopt import matrix, solvers,spmatrix
c = matrix([1.,-1.,1.])
G = [ matrix([[-7., -11., -11., 3.],
                  [ 7., -18., -18., 8.],
                  [-2.,  -8.,  -8., 1.]]) ]
G += [ matrix([[-21., -11.,   0., -11.,  10.,   8.,   0.,   8., 5.],
                   [  0.,  10.,  16.,  10., -10., -10.,  16., -10., 3.],
                   [ -5.,   2., -17.,   2.,  -6.,   8., -17.,  8., 6.]]) ]
h = [ matrix([[33., -9.], [-9., 26.]]) ]
h += [ matrix([[14., 9., 40.], [9., 91., 10.], [40., 10., 15.]]) ]
sol = solvers.sdp(c, Gs=G, hs=h)
print(sol['x'])
print(sol['zs'][0])
print(sol['zs'][1])
nodes=set(itertools.chain(*graphEdges))
print(nodes)
graphEdges=[[1,i,j] for (i,j) in graphEdges]
data=map(list, zip(*(map(list,graphEdges))))

spMat=spmatrix(data[0],data[1],data[2])
print(spMat)
c=matrix([1*])