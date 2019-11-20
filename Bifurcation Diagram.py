
import numpy as np
import matplotlib.pyplot as plt

### INITIALIZATION ##########

def f(x,a):
    return a*x*(1-x)

a_min = 3.63
a_max = 3.65
n_a = 2000
min_iter = 100
n_iter = 200

x_vec = np.zeros(n_iter - min_iter)
y_vec = np.zeros(n_iter - min_iter)
a_vec = np.linspace(a_min,a_max,n_a)


for ii in range(n_a):
    y = 0.5
    
    for jj in range(min_iter):
        y = f(y,a_vec[ii])
    
    for jj in range(n_iter - min_iter):
        y = f(y,a_vec[ii])
        x_vec[jj] = a_vec[ii]
        y_vec[jj] = y
        
    plt.plot(x_vec,y_vec,'*')

# LABEL PLOT #################
plt.title('Equation: $f(x,a) = ax(1-x)$')
plt.xlabel('a value with x = 0.5')
plt.ylabel('$F(x,a)$')
plt.show()
    









