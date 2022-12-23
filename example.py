import numpy as np
import spaceform_pca_lib as sfpca
import scipy.linalg
##############################################################
class parameters:
    def __init__(self):
        self.N = 1000 ## number of points
        self.D = 10 ## input dimension
        self.d = 1 ## target dimension
        self.sigma = .01 # noise std
param = parameters()
##############################################################

# generate random hyperbolic points X, and subspace S, input noise noise_lvl_input
X , S, noise_lvl_input = sfpca.random_hyperbolic_data(param)
# run sfpca
X_, S_ = sfpca.estimate_hyperbolic_subspace_pga(X,param)
# compute output error
noise_lvl_output = sfpca.compute_H_noise_lvl(X_,S)

print(noise_lvl_output)
##############################################################

# generate random spherical points X, and subspace S, input noise noise_lvl_input
X , S, noise_lvl_input = sfpca.random_spherical_data(param)
# run sfpca
X_, S_ = sfpca.estimate_spherical_subspace(X,param)
# compute output error
noise_lvl_output = sfpca.compute_noise_lvl(X_,S)

print(noise_lvl_output)

