import numpy as np
import oapackage as oa
import src.mldoe.design as des


# HELPER FUNCTIONS ------------------------------------------------------
def nauty_reduction(candi_set: list, resolution: int = 3) -> list:
    """
    Remove isomorphism design from a list of candidate designs.

    :param candi_set: list of candidate designs
    :type candi_set: List[design]
    :param resolution: minimal resolution for the candidate designs
    :type resolution: int
    :return: list of the non-isomorphic designs from the input set
    """
    # Turn all arrays into array_link form
    al = [oa.array_link(d.array) for d in candi_set if d.resolution >= resolution]
    # Define the isomorphism classes
    index, _ = selectIsomorphismClasses(al, verbose=0)
    # Select one rep. per class
    _, zz = np.unique(index, return_index=True)
    zz.sort()
    return [candi_set[idx] for idx in list(zz)]


def selectIsomorphismClasses(sols: list, verbose: int = 0) -> tuple:
    """
    Determine the unique isomorphism classes among a set of designs and attribute a class to each member of the set.
    :param sols: list of candidate designs to be sorted
    :type sols: List[design]
    :param verbose: verbosity level
    :type verbose: int
    :return: tuple of the indices and the designs in their canonical form
    :rtype: tuple(List[int],List[np.array])
    """
    # Perform check on array data type
    mm = []
    for ii, al in enumerate(sols):
        if verbose:
            oa.tprint(
                'selectIsomorphismClasses: process array %d/%d' % (ii, len(sols)), dt=4)
        # al = oa.makearraylink(al)
        tt = oa.reduceOAnauty(al)
        alx = tt.apply(al)
        mm.append(np.array(alx))

    # Perform uniqueness check
    nn = len(mm)
    qq = np.array([None] * nn, dtype=object)
    for ii in range(nn):
        qq[ii] = mm[ii].flatten()
    _, indices = np.unique(np.vstack(qq), axis=0, return_inverse=True)
    if verbose >= 1:
        print('selectIsomorphismClasses: %d reduced to %d' %
              (len(sols), np.unique(indices).size))
    return indices, mm


# --------------------------------------------------------------------

def main():
    # Create a 64-run mixed-level design with only basic factors and a single added factor, with a single four-level
    # factor constructed from the three pseudo factors 1,2,3 (constructed using the grouping scheme of Wu 1989).
    root_set = [des.MLD(128, [[1, 2, 3]], [4, 8, 16, i]) for i in range(1, 32) if i not in [1, 2, 3, 4, 8, 16]]
    parent_set = nauty_reduction(root_set)

    # Initialize candidate list
    candidate_lst = []
    min_res = 4
    # Find candidates for each parent
    for parent in parent_set:
        # Consider generators that have length >= 3 as added factors
        gen_list = parent.generators(resolution=min_res)
        # For each generator, compute the DOP and check that the parent design has MA over all DOP
        parent_wlp = parent.wlp
        for gen in gen_list:
            candidate = des.MLD(parent.n_runs, parent.pf_lst, parent.cols + [gen])
            MA = True
            for dop in candidate.dop():
                dop_wlp = dop.wlp
                for i, x in enumerate(dop_wlp):
                    if parent_wlp[i] < dop_wlp[i]:
                        break
                    elif parent_wlp[i] > dop_wlp[i]:
                        MA = False
                        break
                if not MA:
                    break
            if MA:
                candidate_lst.append(candidate)

    # Run the list through the isomorphism selection algorithm
    iso_lst = nauty_reduction(candidate_lst, min_res)
    print(f'{len(parent_set)} parent designs')
    print(f'{len(candidate_lst)} candidates with resolution <= {min_res} generated')
    print(f'{len(iso_lst)} non-isomorphic designs found')


if __name__ == "__main__":
    import cProfile
    with cProfile.Profile() as pr:
        main()
    pr.print_stats(sort='cumulative')

