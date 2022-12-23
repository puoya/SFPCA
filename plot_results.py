import numpy as np
import matplotlib.pyplot as plt


area = 0.1
width = 1
index = 2
#experiment = "std"
experiment = "N"
#experiment = "d"
#experiment = "do"
if experiment == "std":
    data = np.load('std_exp.npy')
    ###################################################
    std_min = 0.05
    std_max = 5.00
    M = np.shape(data)[0]
    x = np.linspace(std_min,std_max,M)
    ###################################################
    plt.plot(x,np.mean(data,0),linewidth=1)
    ###################################################
    colors = np.zeros((M,1))
    varx = 0.05*np.random.uniform(-0.5,0.5,M)
    N = np.shape(data)[1]
    for n in range(N):
        plt.scatter(x[n]+varx,data[:,n], s=area, c=colors)
    ###################################################
    xlabel = "$\sigma$"
    ylabel = "$\overline{d(x_n,\mathbb{S}^d_H)}$"
    ###################################################
elif experiment == "N":
    data = np.load('N_exp.npy')
    ###################################################
    M = np.shape(data)[0]
    varx = 50*np.random.uniform(-0.5,0.5,M)
    N_list = np.arange(1,10)
    N_list = np.concatenate( (100*N_list,1000*N_list, [10000]) )
    N = len(N_list)
    colors = ['#4025f5','#39db77','#db3939']
    sigma = [0.01,0.05,0.1]
    for i in range(3):
        mean = np.mean(data[:,i,:,index],0)
        std = np.std(data[:,i,:,index],0)
        plt.plot(N_list,mean, c=colors[i], linewidth = width, label="$\sigma=$"+str(sigma[i]) )
        for n in range(N):
            plt.scatter(N_list[n]+varx,data[:,i,n,index], s=area, c=colors[i])
        ###################################################
        #print(np.mean(data[:,i,N-1,index]))
    xlabel = "$N$"
    if index == 1:
        ylabel = "$\overline{d(\widehat{x_n},\mathbb{S}^d_{H})}$"
    else:
        ylabel = "$d(\mathbb{S}^d_{\widehat{H}},\mathbb{S}^d_{H})$"
    plt.legend(loc="upper right")
elif experiment == "d":
    data = np.load('d_exp.npy')
    ###################################################
    M = np.shape(data)[0]
    varx = np.random.uniform(-0.5,0.5,M)
    d_list = np.arange(1,10)
    d_list = np.concatenate( (d_list,10*d_list) )
    N = len(d_list)
    ###################################################
    colors = ['#4025f5','#39db77','#db3939']
    sigma = [0.01,0.05,0.1]
    for i in range(3):
        mean = np.mean(data[:,i,:,index],0)
        std = np.std(data[:,i,:,index],0)
        plt.plot(d_list,mean, c=colors[i], linewidth = width, label="$\sigma=$"+str(sigma[i]))
        for n in range(N):
            plt.scatter(d_list[n]+varx,data[:,i,n,index], s=area, c=colors[i])
    xlabel = "$d$"
    if index == 1:
        ylabel = "$\overline{d(\widehat{x_n},\mathbb{S}^d_{H})}$"
    else:
        ylabel = "$\overline{d(x_n,\mathbb{S}^d_{H})}$"
    plt.legend(loc="upper right")
else:
    data = np.load('D_exp_.npy')
    ###################################################
    M = np.shape(data)[0]
    varx = np.random.uniform(-0.5,0.5,M)
    d_list = np.arange(1,10)
    d_list = np.concatenate( (d_list,10*d_list) )
    d_list = np.concatenate( (d_list,[100]) )
    d_list = np.delete(d_list, 0) 
    N = len(d_list)
    ###################################################
    colors = ['#4025f5','#39db77','#db3939']
    sigma = [0.01,0.05,0.1]
    for i in range(3):
        mean = np.mean(data[:,i,:,index],0)
        std = np.std(data[:,i,:,index],0)
        plt.plot(d_list,mean, c=colors[i], linewidth = width, label="$\sigma=$"+str(sigma[i]))
        for n in range(N):
            plt.scatter(d_list[n]+varx,data[:,i,n,index], s=area, c=colors[i])
    xlabel = "$D$"
    if index == 0:
        ylabel = "$\overline{d(x_n,\mathbb{S}^d_{H})}$"
    elif index == 1:
        ylabel = "$\overline{d(\widehat{x_n},\mathbb{S}^d_{H})}$"
    else:
        ylabel = "$d(\mathbb{S}^d_{\widehat{H}} ,\mathbb{S}^d_{H})$"
    plt.legend(loc="upper right")

plt.xlabel(xlabel)
plt.ylabel(ylabel)
plt.show()