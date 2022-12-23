import sys
sys.path.append('../')
import numpy as np
import spaceform_pca_lib as sfpca
import scipy.linalg
##############################################################
class parameters:
    def __init__(self):
        self.N = 1000 ## no. of points
        self.D = 100 ## input dimension
        self.d = 10 ## target dimension
        self.sigma = 1 # noise std
param = parameters()
##############################################################
X , S, noise_lvl = sfpca.random_spherical_data(param)
X_, S_ = sfpca.estimate_spherical_subspace(X,param)
##############################################################
H = S.H
noise_lvl_ = np.linalg.norm(np.matmul(H.T,X_),2,axis = 0)
noise_lvl_ = np.minimum(noise_lvl_,1)
noise_lvl_ = np.arccos(noise_lvl_)
noise_lvl_ = np.mean(noise_lvl_)
##############################################################    
print(noise_lvl)
print(noise_lvl_)