import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as colors
from mpl_toolkits.axes_grid1 import make_axes_locatable
import os
from .NNClass import NNClass

class MNIST(object):
	def __init__(self,Hidden=[10],Split=[0.8,0.1,0.1]):
		'''
		This is a simple object which uses 10,000 samples from the 
		MNIST dataset to test the NNClass object.
		
		Inputs
		======
		Hidden : list
			A list defining the number of nodes in each hidden layer.
		Split : list
			3-element list, where each elements corresponds to the 
			proportion of the dataset to be used for training, 
			validation and testing, respectively.
			
		'''
		
		#read the labels
		self._ReadImages()
		
		#read the images
		self._ReadLabels()
		
		#split data
		self._SplitData(Split)
		
		#create the network object
		s = np.concatenate(([self.X.shape[1]],Hidden,[self.k]))
		self.net = NNClass(s)
		
		#add data to network
		self.net.AddData(self.Xt,self.yt)
		self.net.AddValidationData(self.Xc,self.yc)
		self.net.AddTestData(self.Xtest,self.ytest)
		
		self.trained = False
		
		
	def _ReadLabels(self):
		'''
		Read the labels file.
		
		'''
		#this is the small 10k sample
		fname = os.path.dirname(__file__)+'/__data/MNIST/t10k-labels.idx1-ubyte'
		
		#read the labels from the file
		f = open(fname,'rb')
		MagicNumber = np.fromfile(f,dtype='>i4',count=1)[0]
		self.m = np.fromfile(f,dtype='>i4',count=1)[0]
		self.y = np.fromfile(f,dtype='>u1',count=self.m).astype('int32')
		f.close()
		self.classes = np.unique(self.y)
		self.k = np.size(self.classes)
		
	def _ReadImages(self):
		'''
		Read the images file.
		
		'''
		#this is the small 10k sample
		fname = os.path.dirname(__file__)+'/__data/MNIST/t10k-images.idx3-ubyte'
		
		#read the labels from the file
		f = open(fname,'rb')
		MagicNumber = np.fromfile(f,dtype='>i4',count=1)[0]
		self.m = np.fromfile(f,dtype='>i4',count=1)[0]
		self.nrow = np.fromfile(f,dtype='>i4',count=1)[0]
		self.ncol = np.fromfile(f,dtype='>i4',count=1)[0]
		self.X = np.fromfile(f,dtype='>u1',count=self.m*self.nrow*self.ncol).astype('float32').reshape((self.m,self.nrow*self.ncol))/255.0
		f.close()
		
	def _SplitData(self,Split):
		'''
		Split data into train, validation and test sets.
		
		'''
		#make sure it all adds to one
		s = np.array(Split[:3])/np.sum(Split[:3])
		
		#calculate the number of samples in each bin
		self.mt = np.int(s[0]*self.m)
		self.mc = np.int(s[1]*self.m)
		self.mtest = self.m - (self.mt +self.mc)
		
		#randomize
		srt = np.arange(self.m)
		np.random.shuffle(srt)
		self.X = self.X[srt]
		self.y = self.y[srt]
		
		#now split them
		self.Xt = self.X[:self.mt]
		self.Xc = self.X[self.mt:self.mt+self.mc]
		self.Xtest = self.X[self.mt+self.mc:]
		self.yt = self.y[:self.mt]
		self.yc = self.y[self.mt:self.mt+self.mc]
		self.ytest = self.y[self.mt+self.mc:]
		
	def Train(self,nEpoch,BatchSize=None):
		'''
		Train the network.
		'''
		
		self.net.Train(nEpoch,BatchSize=BatchSize)
		self.trained = True
		
	def PlotSample(self,i,fig=None,maps=[1,1,0,0]):
		'''
		Plot one of the samples.
		'''
		
		scale = [0.0,1.0]
		norm = colors.Normalize(vmin=scale[0],vmax=scale[1])
		
		if fig is None:
			fig = plt
			fig.figure()
		if hasattr(fig,'Axes'):	
			ax = fig.subplot2grid((maps[1],maps[0]),(maps[3],maps[2]))
		else:
			ax = fig	
			
		x = np.arange(self.ncol+1)/self.ncol	
		y = np.arange(self.nrow+1)/self.nrow	
		xg,yg = np.meshgrid(x,y)
		
		grid = self.X[i].reshape((self.ncol,self.nrow))[::-1]
		
		sm = ax.pcolormesh(xg,yg,grid,cmap='Greys',norm=norm)
		
		
		
		ax.text(0.1,0.9,'Class: {:d}'.format(self.y[i]),color='blue',ha='left')

		if self.trained:
			y,p,c = self.Predict(np.array([self.X[i]]))

			ax.text(0.1,0.8,'Predicted: {:d}'.format(c[0] % 10),color='red',ha='left')
		
		
		return ax
		
		
	def PlotRandomSample(self,fig=None,maps=[1,1,0,0]):
		'''
		Plot a random sample.
		
		'''
		i = np.random.randint(0,self.m)
		return self.PlotSample(i,fig=fig,maps=maps)

	def Predict(self,X):
		'''
		Predict a classification.
		
		'''
		return self.net.Predict(X)
