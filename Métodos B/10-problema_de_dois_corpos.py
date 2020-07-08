from math import *
import matplotlib.pyplot as plt

plt.style.use("ggplot")

#definindo variaveis
global tf, x_in, y_in, vx_in, vy_in, GM, tolerance
tolerance = 1e-4
dt_in = 0.1 #0.01
x_in = 0.
y_in = 4.
velocities_x = [-1/2, -1/4, -0.65, -sqrt(2)/2, -1.]
vy_in = 0.
GM = 1
tf = 300
m = 10
#decidido se baseando no intervalo de m que demorava menos tempo de execucao 
#encontrado no travalho da eq logistica


#definindo funcoes
def plot(step, plot_x, plot_y): #plot_x e plot_y sao listas
    for i in range(len(step)):
        plt.plot(plot_x[i], plot_y[i], label=str(step[i]))

        

def rk2(dt, velx, vely, posx, posy):
    
    r = sqrt(posx**2 + posy**2)
    ax = - GM*(posx/r**3)
    ay = - GM*(posy/r**3)
    
    posx_aux = posx + velx*(dt/2)
    velx_aux = velx + ax*(dt/2)
    posy_aux = posy + vely*(dt/2)
    vely_aux = vely + ay*(dt/2)
    
    r = sqrt(posx_aux**2 + posy_aux**2)
    ax_aux = - GM*(posx_aux/r**3)
    ay_aux = - GM*(posy_aux/r**3)
    
    posx = posx + velx_aux*dt
    velx = velx + ax_aux*dt
    posy = posy + vely_aux*dt
    vely = vely + ay_aux*dt
    
    return posx, posy, velx, vely



def rk4(dt, velx, vely, posx, posy):
    #prim passo
    r = sqrt(posx**2 + posy**2)
    ax = - GM*(posx/r**3)
    ay = - GM*(posy/r**3)
    
    posx_aux1 = posx + velx*(dt/2)
    velx_aux1 = velx + ax*(dt/2)
    posy_aux1 = posy + vely*(dt/2)
    vely_aux1 = vely + ay*(dt/2)
    
    #seg passo
    r = sqrt(posx_aux1**2 + posy_aux1**2)
    ax_aux1 = - GM*(posx_aux1/r**3)
    ay_aux1 = - GM*(posy_aux1/r**3)
    
    posx_aux2 = posx + velx_aux1*(dt/2)
    velx_aux2 = velx + ax_aux1*(dt/2)
    posy_aux2 = posy + vely_aux1*(dt/2)
    vely_aux2 = vely + ay_aux1*(dt/2)
    
    #ter passo
    r = sqrt(posx_aux2**2 + posy_aux2**2)
    ax_aux2 = - GM*(posx_aux2/r**3)
    ay_aux2 = - GM*(posy_aux2/r**3)
    
    posx_aux3 = posx + velx_aux2*(dt/2)
    velx_aux3 = velx + ax_aux2*(dt/2)
    posy_aux3 = posy + vely_aux2*(dt/2)
    vely_aux3 = vely + ay_aux2*(dt/2)
    
    r = sqrt(posx_aux3**2 + posy_aux3**2)
    ax_aux3 = - GM*(posx_aux3/r**3)
    ay_aux3 = - GM*(posy_aux3/r**3)
    
    #completo
    posx = posx + (1/6)*(velx + 2*velx_aux1 + 2*velx_aux2 + velx_aux3)*dt
    velx = velx + (1/6)*(ax + 2*ax_aux1 + 2*ax_aux2 + ax_aux3)*dt    
    posy = posy + (1/6)*(vely + 2*vely_aux1 + 2*vely_aux2 + vely_aux3)*dt
    vely = vely + (1/6)*(ay + 2*ay_aux1 + 2*ay_aux2 + ay_aux3)*dt  

    return posx, posy, velx, vely



def step(t, t_aux, t_rk2, dt):
    current_error = sqrt(abs( ((t - t_aux)**2) - ((t_rk2 - t_aux)**2) ))
    dt_new = dt * ((tolerance/current_error)**(1/3))
    
    return dt_new


plotx = []
ploty = []

for vx_in in velocities_x:
        
    n = 0
    t = 0.
    
    plot_xind = []
    plot_yind = []

    x = x_in
    y = y_in
    vx = vx_in
    vy = vy_in
    dt = dt_in

    while (t<=tf):
        x_aux = x
        y_aux = y
        vx_aux = vx
        vy_aux = vy

        n = n+1
            
        x_rk2, y_rk2, vx_rk2, vy_rk2 = rk2(dt, vx, vy, x, y)  
        x, y, vx, vy = rk4(dt, vx, vy, x, y)
   #        
        if n%m == 0:
            dtx = step(x, x_aux, x_rk2, dt)
            dty = step(y, y_aux, y_rk2, dt)
            dtvx = step(vx, vx_aux, vx_rk2, dt)
            dtvy = step(vy, vy_aux, vy_rk2, dt)
            
            dt_new = min([dtx, dty, dtvx, dtvy])

            if dt_new > 2*dt:
                dt_new = 2*dt
                dt = dt_new

            else:
                dt = dt_new
        
        plot_xind.append(x)
        plot_yind.append(y)
        t = t+dt

    plotx.append(plot_xind)
    ploty.append(plot_yind)


    
plot(velocities_x, plotx, ploty)
plt.legend()
plt.xlim(-20, 10)
plt.ylim(-10, 10)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Trajetórias orbitais")
plt.show()
