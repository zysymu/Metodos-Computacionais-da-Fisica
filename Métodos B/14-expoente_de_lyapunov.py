import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

def algo(dl, l, n, log=False):
    lDerPlot = []
    lPlot = []

    while (l<=4):        
        x = 0.2
        lDer = 0

        for i in range(0, n):
            x = l*x*(1-x)
            der = l*(1 - 2*x)
            lDer += np.log10(np.abs(der))
            lDerPlot.append(lDer/n)
            if log:
                lPlot.append(log10(l))
            else:
                lPlot.append(l)

        l += dl
        #plt.scatter(l, (lDer/n), s=10, c="black")
    plt.scatter(lPlot, lDerPlot, s=0.6)
        
    plt.ylabel(r"$\lambda$")
    plt.xlabel(r"$a$")    
    plt.show()

plt.ylim(-3, 1)
algo(0.01, 0, 100)
