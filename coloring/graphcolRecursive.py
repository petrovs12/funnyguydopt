__author__ = 'stefan'
F=[-1]*nodeCount
colornumber = 0; //number of used colors
neighborsIn
    while (number_of_uncolored_vertex > 0):
        # determine a vertex x of maximal degree in G;
        m = max(a)

        x = len(filter(x in edges))
        colornumber = colornumber + 1;
        F(x) = colornumber;
        NN = set of non-neighbors of x;
        while (cardinality_of_NN > 0){ //Find y in NN to be contracted into x
        maxcn =  1; //becomes the maximal number of common neighbors
        ydegree =  1; //becomes degree(y)
        for every vertex z in NN{
        cn=number of common neighbors of z and x;
        if (cn > maxcn or (cn == maxcn and degree(z) < ydegree)){
            y = z;
            ydegree = degree(y);
            maxcn = cn;
            }
        }
        if (maxcn == 0){ //in this case G is unconnected
            y=vertex of maximal degree in NN;
        }
        F(y) = colornumber;
        contract y into x;
        update the set NN of non-neighbors of x;
    }
    G = G   x; //remove x from G
}