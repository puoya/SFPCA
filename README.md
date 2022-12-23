# Space Form Principal Component Analysis

This is the Python implementation of SFPCA: 
> **Principal Component Analysis in Space Froms**\
> Puoya Tabaghi, Michael Khanzadeh, Yusu Wang, Siavash Mirarab\
> University of California San Diego\
> **Abstract.** Principal component analysis (PCA) is a workhorse of modern data science. Practitioners typically perform PCA assuming the data conforms to Euclidean geometry. However, for specific data types, such as hierarchical data, other geometrical spaces may be more appropriate. We study PCA in space forms; that is, those with constant positive (spherical) and negative (hyperbolic) curvatures, in addition to zero-curvature (Euclidean) spaces. At any point on a Riemannian manifold, one can define a Riemannian affine subspace based on a set of tangent vectors and use invertible maps to project tangent vectors to the manifold and vice versa. Finding a low-dimensional affine subspace for a set of points in a space form amounts to dimensionality reduction because, as we show, any such affine subspace is isometric to a space form of the same dimension and curvature. To find principal components, we seek an affine subspace that best represents a set of manifold-valued data points with the minimum distortion after projecting each point onto the affine subspace. We propose specific cost functions that brings about two major benefits: (1) the affine subspace can be estimated by solving an eigenequation --- similar to that of Euclidean PCA, and (2) optimal affine subspaces of different dimensions form a nested set. These properties provide advances over existing comparable methods which are mostly iterative algorithms with slow convergence and weaker theoretical guarantees. Specifically for hyperbolic PCA, the associated eigenequation operates in the Lorentzian space, endowed with an indefinite inner product;  we thus establish a connection between hyperbolic and Euclidean eigenequations. We evaluate the proposed space form PCA (SFPCA) on data sets simulated in spherical and hyperbolic spaces and show that it outperforms alternative methods in convergence speed or accuracy, often both.


## Usage 

### Example

Refer to example.py for spherical and hyperbolic PCA examples on randonly generated data points.

```
python3 example.py 

parameters:
  param.N               number of data points
  param.D               ambient dimension of space form
  param.d               dimension of affine subspace
  param.sigma           input noise level
```

#### 1. Generate data points
```
X,S, noise_lvl_input = sfpca.random_hyperbolic_data(param) 
# or
X,S, noise_lvl_input = sfpca.random_spherical_data(param)
```
Outputs: 
```
  X                     a (D+1) by N matrix of data points 
  S                     the subspace class: contains the base point, tangent subspace, and the slice-unitary matrix
  noise_lvl_input       average distance between noisy input data and the true subspace 
```

#### 2. Estimate affine subspace
```
X_, S_ = sfpca.estimate_hyperbolic_subspace_pga(X,param)
# or
X_, S_ = sfpca.estimate_spherical_subspace_pga(X,param)
```
Outputs: 
```
  X_                     a (D+1) by N matrix of  projected data points
  S_                     estimated subspace class: estimated base point, tangent subspace, and the slice-unitary matrix
```
#### 3. Compute output error
```
noise_lvl_output = sfpca.compute_H_noise_lvl(X_,S)
# or
noise_lvl_output = sfpca.compute_noise_lvl(X_,S)
```
Output: 
```
  noise_lvl_output      average distance between projected data and the true subspace 
```
