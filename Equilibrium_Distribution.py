import numpy as np
import matplotlib.pyplot as plt

### INITIALIZATION ##########

def f(x,a):
    return a*x*(1-x)


n_a =  1 #7
min_iter = 100
n_iter = 100000

x_vec = np.zeros(n_iter - min_iter)
y_vec = np.zeros(n_iter - min_iter)
a_vec = np.array([3.64]) # np.array([3.64,3.68,3.72,3.8,3.9,3.99,3.9999]) 

### Histogram Info ###
n_bins = 100
######################

for ii in range(n_a):
    y = 0.5
    
    for jj in range(min_iter):
        y = f(y,a_vec[ii])
    
    for jj in range(n_iter - min_iter):
        y = f(y,a_vec[ii])
        x_vec[jj] = a_vec[ii]
        y_vec[jj] = y
        
    plt.hist(y_vec,np.linspace(0,1,n_bins+1),alpha = 0.5)

# LABEL PLOT #################
plt.title('Equation: $f(x,a) = ax(1-x)$')
plt.xlabel('$F(x,a)$')
plt.ylabel('Frequency')
plt.show()