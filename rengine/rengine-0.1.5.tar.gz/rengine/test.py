from rengine import CollaborativeFiltering
import numpy as np
clf = CollaborativeFiltering()

print(clf.cos_similarity(
    np.array([5, 4, 0, 0]),  [[1, 0, 3, 2],  [2, 1, 1, 0],  [4, 5, 0, 1]], centered=False))
