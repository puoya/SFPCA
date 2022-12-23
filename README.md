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
python3 main.py 

parameters:
  param.N               number of data points
  param.D               ambient dimension of space form
  param.d               dimension of affine subspace
  param.sigma           input noise level
```
### Examples

#### 1. Run HoroPCA on the smalltree dataset:
```
python main.py --dataset smalltree --model horopca --dim 10 --n-components 2
```
Output: 
```
distortion: 	0.19 +- 0.00
frechet_var: 	7.15 +- 0.00
```

#### 2. Run Euclidean PCA on the smalltree dataset:
```
python main.py --dataset smalltree --model pca --dim 10 --n-components 2
```
Output: 
```
distortion: 	0.84 +- 0.00
frechet_var:    0.34 +- 0.00
```


