import numpy as np
from IGTS import *

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

X = chickendance1

Xt = np.transpose(X)
DP_TT,_ =DP_IGTS(Xt, 7,1,1)
print('Dynamic Programming extracted TT >>>' , DP_TT)