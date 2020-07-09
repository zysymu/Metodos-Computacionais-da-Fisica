import matplotlib.pyplot as plt
from math import *

plt.style.use("ggplot")

global m, l, g, omega, tf, passo
m, l, g = 10., 10., 10.
omega = g/l
tf = 30.
passo = 0.1

#funcoes:
def plot(step, plot_x, plot_y, xlab, ylab): #plot_x e plot_y sao listas
    for i in range(len(step)):
        plt.plot(plot_x[i], plot_y[i], label=str(step[i]))
    
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.legend()
    plt.show()


def energy(vel, pos):
    kinetic = ((1/2)* m* (l**2)* (vel**2)) 
    potential = (m* g* l* (1-cos(pos)))
    total = kinetic + potential
    
    return total



def esp_fase(vel_in, positions, verlet):
    #pos_in eh a lista das posicoes iniciais
    #verlet = True usa Verlet; verlet = False usa Velocity Verlet
    #energy = True calcula energia; energy = False calcula espaco de fase
    
    pos_plot = []
    vel_plot = []
    energ_plot = []
    t_plot = []
    
    if verlet==True:
        for pos in positions:
            vel = vel_in
            t = 0.
            pos_ind = []
            vel_ind = []
            energ_ind = []
            t_ind = []
            
            pos_m1 = pos - vel*passo
            while(t<tf):
                acc = -omega*sin(pos)
                
                pos_p1 = 2*pos - pos_m1 + acc*(passo**2)
                pos_ind.append(pos_p1)
                
                vel = (pos_p1 - pos_m1)/(2*passo)
                vel_ind.append(vel)
                
                E = energy(vel, pos_p1)
                energ_ind.append(E)
                t_ind.append(t)
                
                t = t + passo
                
                pos_m1 = pos
                pos = pos_p1
            
            pos_plot.append(pos_ind)
            vel_plot.append(vel_ind)
            energ_plot.append(energ_ind)
            t_plot.append(t_ind)
            
    else: #varlet==False, usa velocity verlet
        for pos in positions:
            vel = vel_in
            t = 0.
            pos_ind = []
            vel_ind = []
            energ_ind = []
            t_ind = []
            
            acc = -omega*sin(pos)
            while(t<tf):
                vel_phalf = vel + acc*(passo/2)
                pos = pos + vel_phalf*passo
                pos_ind.append(pos)
                
                acc = -omega*sin(pos)
                vel = vel_phalf + acc*(passo/2)
                vel_ind.append(vel)
                
                E = energy(vel, pos)
                energ_ind.append(E)
                t_ind.append(t)
                
                t = t + passo
                
            pos_plot.append(pos_ind)
            vel_plot.append(vel_ind)
            energ_plot.append(energ_ind)
            t_plot.append(t_ind)
            
        
    return pos_plot, vel_plot, energ_plot, t_plot
    

#===============================================================================
#1)
big = [1., 1.5, 3.]

#verlet
pos_bigv, vel_bigv, energ_bigv, t_bigv = esp_fase(vel_in=0, positions=big, verlet=True)
                                                  

plot(big, pos_bigv, vel_bigv, xlab="posicao", ylab="velocidade")

#velocity verlet
pos_bigvv, vel_bigvv, energ_bigvv, t_bigvv = esp_fase(vel_in=0, positions=big, verlet=False)
                                                  

plot(big, pos_bigvv, vel_bigvv, xlab="posicao", ylab="velocidade")

#energia
plot(big, t_bigv, energ_bigv, xlab="tempo", ylab="energia")
plot(big, t_bigvv, energ_bigvv, xlab="tempo", ylab="energia")

print("parte 1 terminou")


#===============================================================================
#2)
pos1 = [-9.42477]

#verlet
pos_pos1v, vel_pos1v, energ_pos1v, t_pos1v = esp_fase(vel_in=0.2, positions=pos1, verlet=True)
                                                  

plot(pos1, pos_pos1v, vel_pos1v, xlab="posicao", ylab="velocidade")

#velocity verlet
pos_pos1vv, vel_pos1vv, energ_pos1vv, t_pos1vv = esp_fase(vel_in=0.2, positions=pos1, verlet=False)
                                                  

plot(pos1, pos_pos1vv, vel_pos1vv, xlab="posicao", ylab="velocidade")

#energia
plot(pos1, t_pos1v, energ_pos1v, xlab="tempo", ylab="energia")
plot(pos1, t_pos1vv, energ_pos1vv, xlab="tempo", ylab="energia")

print("final primeira posicao parte 2")

pos2 = [9.42477]
#verlet
pos_pos2v, vel_pos2v, energ_pos2v, t_pos2v = esp_fase(vel_in=-0.2, positions=pos2, verlet=True)
                                                  

plot(pos2, pos_pos2v, vel_pos2v, xlab="posicao", ylab="velocidade")

#velocity verlet
pos_pos2vv, vel_pos2vv, energ_pos2vv, t_pos2vv = esp_fase(vel_in=-0.2, positions=pos2, verlet=False)
                                                  

plot(pos2, pos_pos2vv, vel_pos2vv, xlab="posicao", ylab="velocidade")

#energia
plot(pos2, t_pos2v, energ_pos2v, xlab="tempo", ylab="energia")
plot(pos2, t_pos2vv, energ_pos2vv, xlab="tempo", ylab="energia")
