import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

x = 10.
tau = 2.
intervalos = [0.1, 0.5, 2., 4.] #cada intervalo eh um delta, inicialmente
delta = 0.5

tf = float(input("coloque o tempo final: "))
t = 0.

tempos = []
res = []

temp_graf = []
res_graf = []

ta = np.arange(0, tf, 0.01)
xa = x * np.exp(-ta/tau)

for delta in intervalos:
    while t <= tf:
        x = x / (1 + (delta/tau))
        tempos.append(t)
        res.append(x)
        t = t + delta
    
    t = 0.
    x = 10.
    temp_graf.append(tempos)
    res_graf.append(res)
    
    tempos = []
    res = []
    
for i in range(len(intervalos)):
    print(temp_graf[i], res_graf[i])
    
for j in (range(len(intervalos))):
    plt.plot(temp_graf[j], res_graf[j], label=str(intervalos[j]), linestyle="--")
  
plt.plot(ta, xa, label="analitica", c="black")
    
plt.xlabel("Tempo")
plt.ylabel("Numero de atomos")
plt.legend()
plt.show()

