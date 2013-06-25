__author__ = 'stefan'

from cvxopt import matrix, spmatrix, log, mul, blas, lapack, amd, cholmod

def covsel(Y):
    """
    Returns the solution of

         minimize    -log det K + Tr(KY)
         subject to  K_{ij}=0,  (i,j) not in indices listed in I,J.

    Y is a symmetric sparse matrix with nonzero diagonal elements.
    I = Y.I,  J = Y.J.
    """

    I, J = Y.I, Y.J
    n, m = Y.size[0], len(I)
    N = I + J*n         # non-zero positions for one-argument indexing
    D = [k for k in range(m) if I[k]==J[k]]  # position of diagonal elements

    # starting point: symmetric identity with nonzero pattern I,J
    K = spmatrix(0.0, I, J)
    K[::n+1] = 1.0

    # Kn is used in the line search
    Kn = spmatrix(0.0, I, J)

    # symbolic factorization of K
    F = cholmod.symbolic(K)

    # Kinv will be the inverse of K
    Kinv = matrix(0.0, (n,n))

    for iters in range(100):

        # numeric factorization of K
        cholmod.numeric(K, F)
        d = cholmod.diag(F)

        # compute Kinv by solving K*X = I
        Kinv[:] = 0.0
        Kinv[::n+1] = 1.0
        cholmod.solve(F, Kinv)

        # solve Newton system
        grad = 2*(Y.V - Kinv[N])
        hess = 2*(mul(Kinv[I,J],Kinv[J,I]) + mul(Kinv[I,I],Kinv[J,J]))
        v = -grad
        lapack.posv(hess,v)

        # stopping criterion
        sqntdecr = -blas.dot(grad,v)
        print("Newton decrement squared:%- 7.5e" %sqntdecr)
        if (sqntdecr < 1e-12):
            print("number of iterations: ", iters+1)
            break

        # line search
        dx = +v
        dx[D] *= 2      # scale the diagonal elems
        f = -2.0 * sum(log(d))    # f = -log det K
        s = 1
        for lsiter in range(50):
            Kn.V = K.V + s*dx
            try:
                cholmod.numeric(Kn, F)
            except ArithmeticError:
                s *= 0.5
            else:
                d = cholmod.diag(F)
                fn = -2.0 * sum(log(d)) + 2*s*blas.dot(v,Y.V)
                if (fn < f - 0.01*s*sqntdecr):
                     break
                s *= 0.5

        K.V = Kn.V

    return K


import numpy as np

A = spmatrix([0,2,-1,2,-2,1], [0,1,2,0,2,1], [0,0,0,1,1,2])
b_symm = (A + A.T)/2



A = spmatrix([10,3,5,-2,5,2], [0,2,1,2,2,3], [0,0,1,1,2,3])
print(A)
print(covsel(A))