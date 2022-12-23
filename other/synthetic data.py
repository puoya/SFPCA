import sys
sys.path.append('../')
import numpy as np
import matplotlib.pyplot as plt
import spaceform_pca_lib as sfpca
import scipy.linalg
##############################################################
eps = 10**(-10)
##############################################################
N = 10000
D = 100
d = 1
sigma = 1
##############################################################
Cx,_, _,H = sfpca.random_spherical_data(N,D,d,sigma)
_,_,H_ = sfpca.estimate_spherical_subspace(Cx,d)
T = np.matmul(H.T, H_)
SVs = scipy.linalg.svdvals(T)
max_SV = np.max(SVs)
dist =  np.arccos(max_SV-eps)- eps/np.sqrt( 1-(max_SV-eps)**2) 
print(dist)


###########################################################################
# def dist(x,p):
#     d = np.arccos(np.inner(x.T,p.T))[0][0]
#     return d
###########################################################################
# def log(x,p):
#     theta = dist(x,p)
#     tx = (theta/np.sin(theta)) *(x - p *np.cos(theta))
#     return tx
###########################################################################