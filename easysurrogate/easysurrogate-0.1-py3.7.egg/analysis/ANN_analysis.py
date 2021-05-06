"""
CLASS TO PERFORM ANALYSIS ON RESULTS FROM A STANDARD ARTIFICIAL NEURAL NETWORK
"""
from .base import BaseAnalysis
import os
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm
from matplotlib import animation
# from sklearn.neighbors import KernelDensity


class ANN_analysis(BaseAnalysis):
    """
    ANN analysis class
    """

    def __init__(self, ann_surrogate, **kwargs):
        print('Creating ANN_analysis object')
        self.ann_surrogate = ann_surrogate

    def make_movie(self, frames=None):
        """
        Makes a move using the training data. Show woth the time evolution of the training data
        and the ANN prediction. Saves the movie to a .gif file.

        Parameters

        n_frames (int): default is 500
            The number of frames to use in the movie.

        Returns: None
        """
        
        if frames is None:
            frames = np.arange(500)
        n_frames = frames.size

        # get the (normalized, time-lagged) training data from the neural network
        X = self.ann_surrogate.surrogate.X
        y = self.ann_surrogate.surrogate.y

        print('===============================')
        print('Making movie...')

        # list to store the movie frames in
        ims = []
        fig = plt.figure(figsize=[4, 4])
        ax1 = fig.add_subplot(111, xlabel=r'$time step$', ylabel=r'y')
        plt.tight_layout()

        # number of features
        n_feat = X.shape[1]
        # allocate memory
        samples = np.zeros([n_frames, self.ann_surrogate.surrogate.n_out])
        idx = 0

        # make movie by evaluating the network at TRAINING inputs
        for i in frames:

            # draw a random sample from the network
            samples[idx] = self.ann_surrogate.surrogate.feed_forward(X[i].reshape([1, n_feat])).flatten()

            # create a single frame, store in 'ims'
            plt1 = ax1.plot(y[frames[0]:i, 0], 'ro', label=r'data')
            plt2 = ax1.plot(samples[0:idx+1, 0], 'g', label='ann prediction')

            if idx == 0:
                ax1.legend(loc=1, fontsize=9)

            ims.append((plt1[0], plt2[0],))
            
            idx += 1

        # make a movie of all frame in 'ims'
        im_ani = animation.ArtistAnimation(fig, ims, interval=20,
                                           repeat_delay=2000, blit=True)
        im_ani.save('ann.gif')
        print('done. Saved movie to ann.gif')
