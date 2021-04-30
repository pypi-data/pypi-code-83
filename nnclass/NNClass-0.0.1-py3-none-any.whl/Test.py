import numpy as np
from .MNIST import MNIST

def Test():
	'''
	This will train a network to classify the MNIST dataset.
	
	'''
	
	mnist = MNIST()
	
	mnist.Train(100)
	
	mnist.net.PlotAccuracy()
	mnist.net.PlotCost()
	
	print('run mnist.PlotRandomSample()')
	mnist.PlotRandomSample()
	
	return mnist
