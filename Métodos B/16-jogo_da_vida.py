import numpy as np
import matplotlib.pyplot as plt

plt.style.use("ggplot")

N = 5 #board dimensions
zmin = 2
zmax = 4
f = .6

s = np.zeros((N,N))

for el in np.nditer(s, op_flags=['readwrite']):
    if np.random.random() < f:
        el[...] = 1

smed=0
for t in range(15): #time loop
    smed_tm = smed
    smed = 0
    sa = np.copy(s)
    for i in range(0,N):
        for j in range(0,N):
            z = 0

            for k in [-1,0,1]:
                for l in [-1,0,1]:
                    m = (i+k+N)%N
                    n = (j+l+N)%N
                    z = z + sa[m,n]
            #end

            if (z>=zmin) and (z<=zmax):
                s[i,j] = 1
            else:
                smed += s[i,j]
                s[i,j] = 0
                
    #end
    print(s, "\n") 
    plt.scatter( (smed/N**2), (smed_tm/N**2) ) 

plt.xlabel("$s med_{t}$")
plt.ylabel("$s med_{t_+1}$")
plt.show()

                

