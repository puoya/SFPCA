import sys
sys.path.append('../')

import numpy as np
import matplotlib.pyplot as plt
import spaceform_pca_lib as sfpca
import scipy.linalg

N = 100
d = 10
K = 2
Cx, H, p,H_full = sfpca.random_spherical_data(N, d, K, 0)
H_, p_,H_full_ = sfpca.estimate_spherical_subspace(Cx, K)
T = np.matmul(H_full.T, H_full_)
SVs = scipy.linalg.svdvals(T)
max_SV = np.max(SVs)
print(max_SV)
#print( np.arccos(np.real(w)+0.000001) )
#print( np.sum(np.arccos(np.real(w)-0.00000001)**2 ) )




################# projection ############################
# Y = np.zeros( (3, N) )\n",
# for n in range(N):\n",
#     x = X[:,n]\n",
#     y = np.inner(x.T,p.T)*p + np.inner(x.T,h.T)*h \n",
#     Y[:,n] = y/np.linalg.norm(y)\n",
# ################# low-dimensional features ##############
# Z = np.zeros( (2, N) )\n",
# for n in range(N):\n",
#     x = Y[:,n]\n",
#     Z[0,n] = np.inner(x.T,p.T)\n",
#     Z[1,n] = np.inner(x.T,h.T)\n",
# fig = plt.figure()\n",
# #ax = fig.add_subplot(projection='3d')\n",
# u = np.linspace(0, 2 * np.pi, 20)\n",
# v = np.linspace(0, np.pi, 20)\n",
# U, V = np.meshgrid(u, v)\n",

# u = np.linspace(0, 2 * np.pi, 20)\n",
# v = np.linspace(0, np.pi, 20)\n",
# U, V = np.meshgrid(u, v)\n",
# x = np.multiply(np.cos(U), np.sin(V))\n",
# y = np.multiply(np.sin(U), np.sin(V))\n",
# z = np.cos(V)\n",
# #ax.plot_wireframe(x, y, z,alpha=0.25, color = 'black',linewidth=0.5)\n",
# #ax.scatter(X[0,:], X[1,:], X[2,:],color = 'red',s=1)\n",
# #ax.scatter(Y[0,:], Y[1,:], Y[2,:],color = 'red',s=1)\n",
# #ax.scatter(V[0,:], V[1,:], V[2,:],color = 'red',s=1)\n",
# #ax.scatter(p[0], p[1], p[2],color = 'black',s=10)\n",

# #ax.set_box_aspect([1,1,1])\n",
# theta = np.linspace(0,2*np.pi,100)\n",
# plt.plot(np.sin(theta), np.cos(theta), color = 'black')\n",
# plt.scatter(Z[0,:],Z[1,:],color = 'red',s=1)\n",
# plt.axis('equal')\n",
# plt.axis('off')\n",
# plt.show()\n",