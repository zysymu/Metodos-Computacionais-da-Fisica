import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

lamb = [0.5, 2, 3, 3.2, 4]

x = np.linspace(0,1)

def f(x):
    return l*x*(1-x)

def g(x):
    return f(f(x)) #ciclo 2

def h(x):
    return g(g(x)) #ciclo 4

plt.ylim(0,1)

for l in lamb:
    plt.plot(x, x, linestyle="--")
    plt.plot(x, f(x), marker=".", label="f(x): ciclo 1")
    plt.plot(x, g(x), marker=".", label="g(x): ciclo 2")
    plt.plot(x, h(x), marker=".", label="h(x): ciclo 4")
    plt.title(r"$\lambda$ = " + str(l))
    plt.legend()
    plt.show()

