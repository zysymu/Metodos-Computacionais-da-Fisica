import matplotlib.pyplot as plt
from math import log10

plt.style.use("ggplot")

def algo(dl, l, log=False):
    xPlot = []
    lPlot = []

    while (l<=4):        
        x = 0.2

        for i in range(0, 100):
            x = l*x*(1-x)

        for i in range(0, 100):
            x = l*x*(1-x)
            xPlot.append(x)
            if log:
                lPlot.append(log10(l))
            else:
                lPlot.append(l)

        l += dl
    
    plt.scatter(lPlot, xPlot, s=0.6)
        
    plt.xlabel(r"$\lambda$")
    plt.ylabel(r"x")    
    plt.show()


algo(0.01, 0)
algo(0.001, 3)
algo(0.001, 3, log=True)
