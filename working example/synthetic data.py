import sys
sys.path.append('../')
import numpy as np
import spaceform_pca_lib as sfpca
import scipy.linalg
##############################################################
class parameters:
    def __init__(self):
        self.N = 10000 ## no. of points
        self.D = 10 ## input dimension
        self.d = 1 ## target dimension
        self.sigma = .01 # noise std
param = parameters()
##############################################################
# parameters to save:
# S, X, noise_lvl_input, param
# for each algorithm save: S_, noise_lvl_output, dist
X , S, noise_lvl_input = sfpca.random_hyperbolic_data(param)
#H1 = S.H
#print(noise_lvl_input)
#print( np.matmul(np.matmul(X.T,J),X) )
#X_, S_ = sfpca.estimate_hyperbolic_subspace(X,param)
X_, S_ = sfpca.estimate_hyperbolic_subspace_pga(X,param)
noise_lvl_output = sfpca.compute_H_noise_lvl(X_,S)
#a = sfpca.subspace_dist_H(S,S_,param)
print(noise_lvl_input)
print(noise_lvl_output)

# X_, S_ = sfpca.estimate_hyperbolic_subspace(X,param)
# noise_lvl_output = sfpca.compute_H_noise_lvl(X_,S)
# print(noise_lvl_output)


# name: spca
# X , S, noise_lvl_input = sfpca.random_spherical_data(param)
# X_, S_ = sfpca.estimate_spherical_subspace(X,param)
# noise_lvl_output = sfpca.compute_noise_lvl(X_,S)
# dist = sfpca.subspace_dist(S,S_)
# print(noise_lvl_input)
# print(noise_lvl_output)
# print(dist)

# name: liu

# X_, S_ = sfpca.estimate_spherical_subspace_liu(X,param)
# noise_lvl_output = sfpca.compute_noise_lvl(X_,S)
# dist = sfpca.subspace_dist(S,S_)
# print(noise_lvl_input)
# print(noise_lvl_output)
# print(dist)


# name: spga
# X_, S_ = sfpca.estimate_spherical_subspace_pga(X,param)
# noise_lvl_output = sfpca.compute_noise_lvl(X_,S)
# dist = sfpca.subspace_dist(S,S_)
# print(noise_lvl_input)
# print(noise_lvl_output)
# print(dist)




# # name: dai
# X_, S_ = sfpca.estimate_spherical_subspace_dai(X,param)
# noise_lvl_output = sfpca.compute_noise_lvl(X_,S)
# dist = sfpca.subspace_dist(S,S_)
# print(noise_lvl_input)
# print(noise_lvl_output)
# print(dist)

# ##############################################################