import numpy as np
import spaceform_pca_lib as sfpca
import scipy.linalg


class parameters:
    def __init__(self):
        self.N = 1000 ## no. of points
        self.D = 5 ## input dimension
        self.d = 1 ## target dimension
        self.sigma = 1 # noise std
param = parameters()

for i in range(10):
    _,p = sfpca.random_J_orthogonal_matrix(param)
    print(p.T)
