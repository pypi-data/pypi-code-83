# Author: Andrew Jewett (jewett.aij at g mail)
# License: MIT License  (See LICENSE.md)
# Copyright (c) 2013


try:
    from .nbody_graph_search import Ugraph
except (ImportError, SystemError, ValueError):
    # not installed as a package
    from nbody_graph_search import Ugraph

# This file defines how dihedral interactions are generated by moltemplate.sh
# by default.  It can be overridden by supplying your own custom file.

#    To find 4-body "dihedral" interactions, we would use this subgraph:
#
#                              1st bond connects atoms 0 and 1
#       *---*---*---*      =>  2nd bond connects atoms 1 and 2
#       0   1   2   3          3rd bond connects atoms 2 and 3
#

bond_pattern = Ugraph([(0, 1), (1, 2), (2, 3)])
# (Ugraph atom indices begin at 0, not 1)


def canonical_order(match):
    """
    Before defining a new interaction, we must check to see if an
    interaction between these same 4 atoms has already been created
     (perhaps listed in a different, but equivalent order).
    If we don't check for this this, we will create many unnecessary redundant
    interactions (which can slow down he simulation).
    To avoid this, I define a "canonical_order" function which sorts the atoms
    and bonds in a way which is consistent with the symmetry of the interaction
    being generated...  Later the re-ordered list of atom and bond ids will be
    tested against the list of atom/bond ids in the matches-found-so-far,
    before it is added to the list of interactions found so far.  Note that
    the energy of a dihedral interaction is a function of the dihedral-angle.
    The dihedral-angle is usually defined as the angle between planes formed
    by atoms 0,1,2 & 1,2,3. This angle does not change when reversing the
    order of the atoms.  So it does not make sense to define a separate
    dihedral interaction between atoms  0,1,2,3   AS WELL AS between   3,2,1,0.
    So we sort the atoms so that the first atom has a lower atomID than the
    last atom.  (Later we will check to see if we have already defined an
    interaction between these 4 atoms.  If not then we create a new one.)

    """

    # match[0][0:3] contains the ID numbers of the 4 atoms in the match
    atom0 = match[0][0]
    atom1 = match[0][1]
    atom2 = match[0][2]
    atom3 = match[0][3]
    # match[1][0:2] contains the ID numbers of the the 3 bonds
    bond0 = match[1][0]
    bond1 = match[1][1]
    bond2 = match[1][2]
    if atom0 < atom3:
        # return ((atom0, atom1, atom2, atom3), (bond0, bond1, bond2))  same
        # as:
        return match
    else:
        return ((atom3, atom2, atom1, atom0), (bond2, bond1, bond0))
