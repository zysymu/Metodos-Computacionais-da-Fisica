import matplotlib.pyplot as plt
from math import *
import numpy as np

plt.style.use("ggplot")

#variaveis
global x_in, tau, t, tf
steps = [0.01, 0.5]
tf = 6
x_in = 10.
tau = 2.

#analitica
ta = np.linspace(0, tf)
xa = x_in * np.exp(-ta/tau)

#funcoes
def plot(step, plot_x, plot_y, xlab, ylab, met): #plot_x e plot_y sao listas
    for i in range(len(step)):
        plt.plot(plot_x[i], plot_y[i], label=str(step[i]) +" "+ met)
    
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    

def time(dt, t):
    tind = []
    while (t<=tf):
        tind.append(t)
        t = t+dt
    
    return tind

    
def heun(dt, x):
    ind = []
    t=0
    while (t<=tf):
        k1 = -(x/tau)
        x_aux = x + k1*dt
        k2 = -(x_aux/tau)
        ind.append(x)
        x = x + (1/2)*(k1+k2)*dt
        t = t+dt
        
    return ind


def midpoint(dt, x):
    ind = []
    t=0
    while (t<=tf):
        k1 = -(x/tau)
        x_aux = x + k1*(dt/2)
        k2 = -(x_aux/tau)
        ind.append(x)
        x = x + k2*dt
        t = t+dt
        
    return ind


def ralston(dt, x):
    ind = []
    t=0
    while (t<=tf):
        k1 = -(x/tau)
        x_aux = x + (3/4)*k1*dt
        k2 = -(x_aux/tau)
        ind.append(x)
        x = x + (1/3)*k1*dt + (2/3)*k2*dt
        t = t+dt
        
    return ind
    
    
heun_plot = []
midpoint_plot = []
ralston_plot = []
t_plot = []

for dt in steps:
    heun_plot.append(heun(dt, x_in))
    midpoint_plot.append(midpoint(dt, x_in))
    ralston_plot.append(ralston(dt, x_in))
    t_plot.append(time(dt, t=0))
    
    

plt.plot(ta, xa, label="analitica", c="black", linewidth=4)
plot(steps, t_plot, heun_plot, xlab="Tempo", ylab="Num atomos", met="Heun")
plot(steps, t_plot, midpoint_plot, xlab="Tempo", ylab="Num atomos", met="PM")
plot(steps, t_plot, ralston_plot, xlab="Tempo", ylab="Num atomos", met="Ralston")

plt.legend()
plt.show()
    
