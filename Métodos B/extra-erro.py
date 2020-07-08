from math import *

dt_min = float(input("passo minimo: "))
dt_max = float(input("passo maximo: "))

tf=30
w=1
x_in=0.1

#rk4
while (dt_min < dt_max):
    x = .1;
    v = 0;
    t = 0;
    ex = 0;
    ev = 0;

    while(t < tf):
        k1x = v
        k1v = -w*x
        
        xn = x + k1x*dt_min*.5
        vn = v + k1v*dt_min*.5
        
        k2x = vn
        k2v = -w*xn
        
        xn = x + k2x*dt_min*.5
        vn = v + k2v*dt_min*.5
        
        k3x = vn
        k3v = -w*xn
        
        xn = x + k3x*dt_min
        vn = v + k3v*dt_min
        
        k4x = vn
        k4v = -w*xn
        
        x = x + (1./6)*(k1x + 2.*k2x + 2.*k3x + k4x)*dt_min
        v = v + (1./6)*(k1v + 2.*k2v + 2.*k3v + k4v)*dt_min
        
        t = t + dt_min;
        
        xa = x_in*cos(w*t)
        va = -x_in*sin(w*t)
        
        ex = ex + (x - xa)
        ev = ev + (v - va)
        
    print("para rk4, temos:\n")
    print(f"{log10(dt_min)},  {log10(abs(ex*(dt_min/tf)))},  {log10(abs(ev*(dt_min*tf)))} \n\n")
    dt_min = 2*dt_min
		

#rk2
while (dt_min < dt_max):
    x = .1;
    v = 0;
    t = 0;
    ex = 0;
    ev = 0;

    while(t < tf):
        k1x = v
        k1v = -w*x
        
        xn = x + k1x*dt_min*.5
        vn = v + k1v*dt_min*.5
        
        k2x = vn
        k2v = -w*xn
        
        x = x + k2x*dt_min
        v = v + k2v*dt_min
        
        t = t + dt_min;
        
        xa = x_in*cos(w*t)
        va = -x_in*sin(w*t)
        
        ex = ex + (x - xa)
        ev = ev + (v - va)
        
    print("para rk2, temos:\n")
    print(f"{log10(dt_min)},  {log10(abs(ex*(dt_min/tf)))},  {log10(abs(ev*(dt_min*tf)))} \n\n")
    dt_min = 2*dt_min


#euler cromer
while (dt_min < dt_max):
    x = .1;
    v = 0;
    t = 0;
    ex = 0;
    ev = 0;

    while(t < tf):
        x = x + v*dt_min
        v = v - w*sin(x)*dt_min
        t = t + dt_min
        
        xa = x_in*cos(w*t)
        va = -x_in*sin(w*t)
        
        ex = ex + (x - xa)
        ev = ev + (v - va)
        
    print("para euler-cromer, temos:\n")
    print(f"{log10(dt_min)},  {log10(abs(ex*(dt_min/tf)))},  {log10(abs(ev*(dt_min*tf)))} \n\n")
    dt_min = 2*dt_min

