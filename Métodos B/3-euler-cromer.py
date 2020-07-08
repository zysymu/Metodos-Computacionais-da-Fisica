from math import *
import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

g = 10.
l = 10.
theta_zero = 0.1
t = 0.

delta = float(input("coloque o valor de delta t: "))
tf = float(input("coloque o valor de tempo final: "))

omega = g/l

plot_theta_exp = []
plot_tempo_exp = []

plot_theta_cro = []
plot_tempo_cro = []

theta = theta_zero

vel = 0.

#euler explicito
while (t<=tf):
    theta_aux = theta
    plot_theta_exp.append(theta)
    theta = theta + vel*delta
    
    vel = vel - omega * sin(theta_aux) * delta
        
    plot_tempo_exp.append(t)
    
    t = t + delta
 

theta = theta_zero
t = 0.
vel = 0.

#euler-cromer
while (t<=tf):
    plot_theta_cro.append(theta)
    theta = theta + vel*delta
    
    vel = vel - omega * sin(theta) * delta
    
    plot_tempo_cro.append(t)
    
    t = t + delta


#analitica
t_a = np.arange(0, tf, 0.01)
sol_a = theta_zero * np.cos(omega*t_a)


#plotandox
plt.plot(plot_tempo_exp, plot_theta_exp, label="explicito")
plt.plot(plot_tempo_cro, plot_theta_cro, label="euler-cromer")
plt.plot(t_a, sol_a, label="analitica", c="black", linestyle="--")
plt.ylabel("angulo")
plt.xlabel("tempo")
plt.legend()
plt.show()
