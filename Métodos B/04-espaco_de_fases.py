import matplotlib.pyplot as plt
from math import *

plt.style.use("ggplot")

delta = 0.1
tf = float(input("valor do tempo final: "))
m, l, g = 10., 10., 10.

#=======================================================
#funcoes:

#func movimento pendular:
def vel_theta(vel, t, angulos, tf):
    vel_aux = vel
    theta_ind = []
    vel_ind = []
    
    plot_vel = []
    plot_theta = []
    
    for el in angulos:
        while (t<=tf):
            el = el + vel_aux * delta
            theta_ind.append(el)
    
            vel_aux = vel_aux - sin(el) * delta
            vel_ind.append(vel_aux)

            
            t = t + delta
    
        t = 0.
        vel_aux = vel
        plot_vel.append(vel_ind)
        plot_theta.append(theta_ind)
        theta_ind = []
        vel_ind = []
        
    return plot_vel, plot_theta



#func plot:
def plot(angulos, plot_x, plot_y, xlab, ylab):
    for i in range(len(angulos)):
        plt.plot(plot_y[i], plot_x[i], label=str(angulos[i]))
    
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend()
    plt.show()
        
        
        
#==================================================================
#velocidades:

#velocidade inicial nula:
theta_nula = [0.1, 1.5, 3.]
plot_vel_nul, plot_theta_nul = vel_theta(vel=0., t=0.,
                                         angulos=theta_nula, tf=tf)

plot(theta_nula, plot_vel_nul, plot_theta_nul, xlab="angulo theta",
     ylab="velocidade (theta ponto)")
    

    
#velocidade inicial nao nula:
theta_val1 = [9.42]
plot_vel_val1, plot_theta_val1 = vel_theta(vel=-0.1, t=0.,
                                         angulos=theta_val1, tf=tf)

theta_val2 = [-9.42]
plot_vel_val2, plot_theta_val2 = vel_theta(vel=0.1, t=0.,
                                         angulos=theta_val2, tf=tf)

for i in range(len(theta_val1)):
        plt.plot(plot_theta_val1[i], plot_vel_val1[i],
                 label=str(theta_val1[i]))
        
for i in range(len(theta_val2)):
		plt.plot(plot_theta_val2[i], plot_vel_val2[i],
                 label=str(theta_val2[i]))
        
plt.xlabel("angulo theta")
plt.ylabel("velocidade (theta ponto)")
plt.legend()        
plt.show()


#==================================================================
#energias:
      
delta_t = [0.1, 0.01]
energ_ind = []
energ_plot = []
t_ind = []
t_plot = []

el = 1.5
t = 0.
vel = 0.1
vel_aux = vel

theta = el
for delta in delta_t:
    while (t<=tf):
        theta = theta + vel_aux * delta
        
        vel_aux = vel_aux - sin(theta) * delta
                   
        energia = ((1/2)* m* (l**2)* (vel_aux**2)) + (m* g* l* (1-cos(theta)))
        energ_ind.append(energia)
            
        t_ind.append(t)    
        t = t + delta
    
    t = 0.
    energia = 0.
    theta = el
    vel_aux = vel
    energ_plot.append(energ_ind)
    t_plot.append(t_ind)
    energ_ind = []
    t_ind = []

plot(delta_t, energ_plot, t_plot, xlab="tempo", ylab="energia total")
