import cvxopt

__author__ = 'stefan'
from cvxopt import matrix
import numpy as np
from array import array
nrowTest=5
A=matrix(1,(1,4))
print(A)
B=cvxopt.normal(nrowTest,nrowTest)
print(B)
A = matrix(array('i', [0,1,2,3]), (2,2))
print(A)
X=matrix(xrange(0,4),(2,2))
print(X)
A1 = matrix([1, 2], (2,1))
B1 = matrix([6, 7, 8, 9, 10, 11], (2,3))
B2 = matrix([12, 13, 14, 15, 16, 17], (2,3))
B3 = matrix([18, 19, 20], (1,3))
C = matrix([[A1, 3.0, 4.0, 5.0], [B1, B2, B3]])
print(C)
# in general spmatrix object can be thought of asa triplet desctiption of a sparce matrix, that is a list of entries of the matrix, with for ech entry th vallue, row index, and col index entries that are not included in the list are assumed to be
#zero for example,
A = cvxopt.spmatrix(1.0, range(4), range(4))
print(A)
# cvxopt.spmatrix takes usually 3 args, that are "zipped" - the 1st argument contains the values, 2nd- row coordinates, 3ed-column coordinates
matr=np.mat("1,2,3;3,4,5")
print(matr)
