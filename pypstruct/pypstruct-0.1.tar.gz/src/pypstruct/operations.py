import math,numpy,subprocess

import xml.etree.ElementTree


def kabsch_rmsd(P, Q):
    """
    Rotate matrix P unto Q and calculate the RMSD
    """
    P = kabsch_rotate(P, Q)
    return rmsd(P, Q)


def kabsch_rotate(P, Q):
    """
    Rotate matrix P unto matrix Q using Kabsch algorithm
    """
    U = kabsch(P, Q)

    # Rotate P
    P = numpy.dot(P, U)
    return P


def kabsch(P, Q):
    """
    The optimal rotation matrix U is calculated and then used to rotate matrix
    P unto matrix Q so the minimum root-mean-square deviation (RMSD) can be
    calculated.

    Using the Kabsch algorithm with two sets of paired point P and Q,
    centered around the center-of-mass.
    Each vector set is represented as an NxD matrix, where D is the
    the dimension of the space.

    The algorithm works in three steps:
    - a translation of P and Q
    - the computation of a covariance matrix C
    - computation of the optimal rotation matrix U

    http://en.wikipedia.org/wiki/Kabsch_algorithm

    Parameters:
    P -- (N, number of points)x(D, dimension) matrix
    Q -- (N, number of points)x(D, dimension) matrix

    Returns:
    U -- Rotation matrix

    """

    # Computation of the covariance matrix
    C = numpy.dot(numpy.transpose(P), Q)

    # Computation of the optimal rotation matrix
    # This can be done using singular value decomposition (SVD)
    # Getting the sign of the det(V)*(W) to decide
    # whether we need to correct our rotation matrix to ensure a
    # right-handed coordinate system.
    # And finally calculating the optimal rotation matrix U
    # see http://en.wikipedia.org/wiki/Kabsch_algorithm
    V, S, W = numpy.linalg.svd(C)
    d = (numpy.linalg.det(V) * numpy.linalg.det(W)) < 0.0

    if d:
        S[-1] = -S[-1]
        V[:, -1] = -V[:, -1]

    # Create Rotation matrix U
    U = numpy.dot(V, W)

    return U


def quaternion_rmsd(P, Q):
    """
    based on doi:10.1016/1049-9660(91)90036-O
    Rotate matrix P unto Q and calculate the RMSD
    """
    rot = quaternion_rotate(P, Q)
    P = numpy.dot(P,rot)
    return rmsd(P, Q)


def quaternion_transform(r):
    """
    Get optimal rotation
    note: translation will be zero when the centroids of each molecule are the
    same
    """
    Wt_r = makeW(*r).T
    Q_r = makeQ(*r)
    rot = Wt_r.dot(Q_r)[:3,:3]
    return rot


def makeW(r1,r2,r3,r4=0):
    """
    matrix involved in quaternion rotation
    """
    W = numpy.asarray([
             [r4, r3, -r2, r1],
             [-r3, r4, r1, r2],
             [r2, -r1, r4, r3],
             [-r1, -r2, -r3, r4] ])
    return W


def makeQ(r1,r2,r3,r4=0):
    """
    matrix involved in quaternion rotation
    """
    Q = numpy.asarray([
             [r4, -r3, r2, r1],
             [r3, r4, -r1, r2],
             [-r2, r1, r4, r3],
             [-r1, -r2, -r3, r4] ])
    return Q


def quaternion_rotate(X, Y):
    """
    Calculate the rotation
    """
    N = X.shape[0]
    W = numpy.asarray([makeW(*Y[k]) for k in range(N)])
    Q = numpy.asarray([makeQ(*X[k]) for k in range(N)])
    Qt_dot_W = numpy.asarray([numpy.dot(Q[k].T,W[k]) for k in range(N)])
    W_minus_Q = numpy.asarray([W[k] - Q[k] for k in range(N)])
    C1 = -numpy.sum(Qt_dot_W,axis=0)
    C2 = 0.5*N
    C3 = numpy.sum(W_minus_Q,axis=0)
    A = numpy.dot(C3.T,C3)*C2-C1
    eigen = numpy.linalg.eigh(A)
    r = eigen[1][:,eigen[0].argmax()]
    rot = quaternion_transform(r)
    return rot


def centroid(X):
    """
    Calculate the centroid from a vectorset X
    """

    C = sum(X)/len(X)
    return C


def rmsd(V, W):
    """
    Calculate Root-mean-square deviation from two sets of vectors V and W.
    """
    D = len(V[0])
    N = len(V)
    rmsd = 0.0
    for v, w in zip(V, W):
        rmsd += sum([(v[i]-w[i])**2.0 for i in range(D)])
    return numpy.sqrt(rmsd/N)


def aliFit(structA, structB, aliArrayOne, aliArrayTwo):
    equiResNum = []
    i = -1
    j = -1

    for x,y in zip(aliArrayOne, aliArrayTwo):
        xBool = False
        yBool = False
        if x != '-' :
            xBool = True
            i += 1
        if y != '-' :
            yBool = True
            j += 1

        if not xBool or not yBool:
            continue
        equiResNum.append( { 'iRes' : { 'num' : i , 'name' : x }, 'jRes' : { 'num' : j , 'name' : y } } )

    print("Superimposing on", str(len(equiResNum)), 'CA coordinates')

    P = [ numpy.array( structA.trace[ d['iRes']['num']].coordinates) for d in equiResNum ]
    Q = [ numpy.array( structB.trace[ d['jRes']['num']].coordinates) for d in equiResNum ]

    normal_rmsd = rmsd(P, Q)

    Pc = centroid(P)
    Qc = centroid(Q)
    P -= Pc
    Q -= Qc

    U = kabsch(P, Q)
    #p_all -= Pc
    #p_all = numpy.dot(p_all, U)
    #write_coordinates(p_atoms, p_all, title="{} translated".format(args.structure_a))
    k_rmsd = kabsch_rmsd(P, Q)
    q_rmsd = quaternion_rmsd(P, Q)

    print ("Normal RMSD:", normal_rmsd)
    print ("Kabsch RMSD:", k_rmsd)
    print ("Quater RMSD:", q_rmsd)
    return (U, normal_rmsd, k_rmsd, q_rmsd)

def fit(structObj1, structObj2, **kwargs):

    mode = "blast"
    aliSeq1 = None
    aliSeq2 = None
    if 'mode' in kwargs:
        mode = kwargs['mode']

    if mode == "needle":
        ali = needle(structObj1, structObj2)
        (aliSeq1, aliSeq2) = ali.aaWords

    elif mode == "blast":
        blastThem(structObj1, structObj2, mode)
        msaObj = clustThem(mode)

        aliSeq1 = msaObj[0]['sequence']
        aliSeq2 = msaObj[1]['sequence']

    print (aliSeq1, "\n", aliSeq2)

    _tuple = aliFit(structObj1, structObj2, aliSeq1, aliSeq2)
    return _tuple


