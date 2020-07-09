import matplotlib.pyplot as plt

global tf, x_in
tf = 50000
deltas = [0.1, 1, 10, 100, 1000, 10000]
x_in = 0.01
#func := dx/dt = 0.0001*x*(2-x)

plt.style.use("ggplot")

#funcoes:
def f(x):
    return 0.0001*x*(2-x)



def plot(step, plot_x, plot_y, met): #plot_x e plot_y sao listas
    for i in range(len(step)):
        plt.plot(plot_x[i], plot_y[i], label=str(step[i]) +" "+ met)



def adamsBash(dt, x_in, predCorr):
    ind = []
    x1 = x_in
    x0 = x_in
    t = 0
    while (t<=tf):
        x2 = x1 + dt*((3/2)*f(x1) - (1/2)*f(x0)) #colocar func
        
        if (predCorr==True):
            x2 = x1 + dt*((5/12)*f(x2) + (2/3)*f(x1) - (1/12)*f(x0))
        
        x0 = x1
        x1 = x2

        ind.append(x2)

        t += dt

    return ind



def time(dt, t):
    tind = []
    while (t<=tf):
        tind.append(t)
        t = t+dt
    
    return tind



ab_graph = [adamsBash(dt, x_in, predCorr=False) for dt in deltas]
pred_corr = [adamsBash(dt, x_in, predCorr=True) for dt in deltas]
t = [time(dt, t=0) for dt in deltas]


plot(deltas, t, ab_graph, met="")
plt.legend()
plt.title("Somente preditor")
plt.show()


plot(deltas, t, pred_corr, met="")
plt.legend()
plt.title("Preditor-Corretor")
plt.show()


