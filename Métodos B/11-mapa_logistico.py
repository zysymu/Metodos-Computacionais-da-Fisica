import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

global xa, ya
xa = np.linspace(0, 1)
ya = xa

#pro a plotamos x_n por n
#pro b plotamos primeiro retorno (x_n por x_n+1)

lamb = [0.5, 2., 3.2, 3.5, 4.]
ciclo = ["ciclo 0", "ciclo 1", "ciclo 2", "ciclo 4", "caos"]
#tipo dicionario, mas como plotar com matplotlib??

x_initial = 0.01


def plot(step, plot_x, plot_y, met, s=False): #plot_x e plot_y sao listas
    if s:
        plt.plot(xa, ya, linestyle="--")
        
        for i in range(len(step)):
            plt.scatter(plot_x[i], plot_y[i], marker=".", label=str(step[i]) +": "+ met[i])
            plt.title("Mapa de primeiro retorno")
            plt.xlabel(r"$x_{n-1}$")
            plt.ylabel(r"$x_{n}$")
            plt.legend()    
        

    else:
        for i in range(len(step)):
            plt.scatter(plot_x[i], plot_y[i], marker=".", label=str(step[i]) +": "+ met[i])
            plt.title("Evolução de x")
            plt.xlabel(r"$n$")
            plt.ylabel(r"$x_{n}$")
            plt.legend()    
    
    plt.show()



x_nPlot = [] #x_{n}
x_nmPlot = [] #x_{n-1}
nPlot = [] #indice

for l in lamb:#dict.values(lamb):
    x = x_initial
    x_n = []
    x_nm = []
    n = []

    for i in range(0, 100):
        x_nm.append(x)
        x = l*x*(1-x)
        x_n.append(x)
        n.append(i)
        

    x_nPlot.append(x_n)
    x_nmPlot.append(x_nm)
    nPlot.append(n)


plot(lamb, nPlot, x_nPlot, met=ciclo) #plotando x_n por n (a)
plot(lamb, x_nmPlot, x_nPlot, met=ciclo, s=True) #plotando mapa primeiro retorno (b)

