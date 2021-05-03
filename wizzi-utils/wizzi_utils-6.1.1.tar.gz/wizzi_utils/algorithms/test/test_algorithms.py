from wizzi_utils.algorithms import algorithms as alg
from wizzi_utils.misc import misc_tools as mt
from wizzi_utils.pyplot import pyplot_tools as pyplt
import numpy as np
# noinspection PyPackageRequirements
import matplotlib.pyplot as plt


def find_centers_test():
    """
    if you get No module named 'sklearn.__check_build._check_build'
    pip uninstall scikit-learn
    pip uninstall sklearn
    pip install sklearn
    :return:
    """
    mt.get_function_name(ack=True, tabs=0)
    A = np.array([[-1, -1], [-1, 1], [1, 1], [1, -1]])
    centers = alg.find_centers(A, k=1)
    if centers is not None:
        data_and_centers = np.concatenate((A, centers))
        colors = [pyplt.get_RGBA_color('g')] * A.shape[0]
        colors.append(pyplt.get_RGBA_color('r'))

        print('\tVisual test: square and it\'s center')
        pyplt.plot_2d_scatter(
            data=data_and_centers,
            colors=colors,
            data_label='KMeans',
            window_title='find_centers_test()',
            legend={'loc': 'upper center', 'ncol': 1, 'fancybox': True, 'framealpha': 0.5, 'edgecolor': 'black'},
            main_title='square and it\'s center',
            loc=(0, 0)
        )
    return


def test_all():
    print('{}{}:'.format('-' * 5, mt.get_base_file_and_function_name()))
    find_centers_test()
    print('{}'.format('-' * 20))
    return
