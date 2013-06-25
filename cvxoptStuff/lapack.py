__author__ = 'stefan'
from cvxopt import matrix, normal
from cvxopt.lapack import gesv, getrs
n = 10
A = normal(n,n)
b = normal(n)
ipiv = matrix(0, (n,1))
x = +b
gesv(A, x, ipiv)               # x = A^{-1}*b
x2 = +b
getrs(A, ipiv, x2, trans='T')  # x2 = A^{-T}*b
x += x2
print(x)
