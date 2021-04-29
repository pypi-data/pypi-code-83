from wizzi_utils.algorithms import algorithms as alg
from wizzi_utils.misc import misc_tools as mt
import matplotlib.pyplot as plt
import numpy as np


def find_centers_test():
    mt.get_function_name(ack=True, tabs=0)
    A = np.array([[-1, -1], [-1, 1], [1, 1], [1, -1]])
    centers = alg.find_centers(A, k=1)
    X, y = mt.de_augment_numpy(A)
    X_c, y_c = mt.de_augment_numpy(centers)
    plt.title('1 mean(of a square) example')
    plt.scatter(X, y, color='g', marker='.', label='A(the points)')
    plt.scatter(X_c, y_c, color='r', marker='o', label='one center({})'.format(centers[0]))
    plt.legend(loc='upper center', ncol=1, fancybox=True, framealpha=0.5, edgecolor='black')
    print('\tVisual test: square and it\'s center')
    plt.show()
    return


def test_all():
    print('{}{}:'.format('-' * 5, mt.get_base_file_and_function_name()))
    find_centers_test()
    print('{}'.format('-' * 20))
    return
