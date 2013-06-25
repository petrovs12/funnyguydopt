__author__ = 'stefan'

from scipy.linalg import *
import numpy as np

N = 20
b = np.random.random_integers(-2000,2000,size=(N,N))
b_symm = (b + b.T)/2
c = np.random.random_integers(-2000,2000,size=(N,N))
c_symm = (b + b.T)/2

moo=eig(b_symm,c_symm)
print(moo)