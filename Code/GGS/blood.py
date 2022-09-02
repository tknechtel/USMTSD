from ggs import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import math
from hmmlearn.hmm import GaussianHMM
from numpy.testing import assert_array_equal, assert_array_almost_equal
import time
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning) 
warnings.filterwarnings("ignore", category=RuntimeWarning)



datapath = "/content/drive/MyDrive/Masterarbeit/Thesis/Data/Datafinal/"
data_img =  "/content/drive/MyDrive/Masterarbeit/Thesis/Data/Datafinal/IMG/"

synthetic_data = np.genfromtxt(datapath + "syn_1400_6_7.csv", skip_header=1, delimiter=',')
synthetic_data = synthetic_data.T
synthetic_data2 = np.genfromtxt(datapath + "syn_1400_12_14.csv", skip_header=1, delimiter=',')
synthetic_data2 = synthetic_data2.T
chickendance1 = np.genfromtxt( datapath + "Chicken19_60min_sample.csv",skip_header=1, delimiter=',')
chickendance2 = np.genfromtxt( datapath + "Chicken21_60min_sample.csv",skip_header=1, delimiter=',')
blood_pig = np.genfromtxt( datapath + "blood_pic.csv",skip_header=1, delimiter=',')
nilm1 =np.genfromtxt( datapath + "nilm1_60min_sample.csv",skip_header=1, delimiter=',')
apple =np.genfromtxt( datapath + "apple.csv",skip_header=1, delimiter=',',usecols= range(1,3))
bee =np.genfromtxt( datapath + "bee.csv",skip_header=1, delimiter=',',usecols= range(1,5))
occ =np.genfromtxt( datapath + "occ.csv",skip_header=1, delimiter=',',usecols= range(1,5))

d = 3 #d-dimensional covariance
numCovs = 3 #Number of segments
samplesPerSeg = 100

#X1 = np.genfromtxt("/content/drive/MyDrive/Masterarbeit/Thesis/Data/data/Synthetic.csv", skip_header=1, delimiter=',')
#X1 = np.genfromtxt("/content/drive/MyDrive/Masterarbeit/Thesis/Data/blood_pic.csv", skip_header=1, delimiter=",")
Xt = np.transpose(blood_pig)

#Generate numCovs random covariances
runSum = 0
for z in range(100):
	np.random.seed(z)
	c = []
	for i in range(numCovs):
		temp = np.random.normal(size=(d,d))
		temp2 = np.dot(temp, temp.T)
		c.append(temp2)


	#Generate synthetic data

	data = np.zeros((numCovs*samplesPerSeg, d))
	for i in range(numCovs):
		for j in range(samplesPerSeg):
			temp = np.random.multivariate_normal(np.zeros(d), c[i])
			data[samplesPerSeg*i + j, :] = temp		

	data = data.T

	#fname = "SynthData_"+str(z)+".txt"
	#np.savetxt(fname, data, fmt='%f', delimiter=',')

	#Run GGS
bps = GGS(Xt, Kmax = numCovs-1, lamb = 10)
print (bps[0][-1])
