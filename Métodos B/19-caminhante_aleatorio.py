import matplotlib.pyplot as plt
import numpy as np

plt.style.use("ggplot")

N = [10, 20, 100, 200] # diferentes numeros de passos

# um caminhante eh a soma de todos os N passos em x que ele da
# a distribuicao dos passos eh o gerador de nums aleatorios. precisamos normalizar pra que fique entre 0 e 1

def generator(r):
     # vai nos dar o proximo x
     # recebe um numero r entre 0 e 1
    #return r*4 -2
    return np.random.random_integers(-1,1)


def walker(N, x_in):
    M = 100 # numero total de caminhantes
    actual_std = []
    theoretical_std = []

    for step in range(M):
        X = [x_in] # comeca com o passo inicial, depois vai dando append
        T = [0] # array com os tempos pra poder plotar depois
        x = x_in
        for t in range(1, N): # loop temporal
            x += generator(np.random.random())
            X.append(x)
            T.append(t)

        plt.plot(T, X)
        actual_std.append(np.std(X))

        sqrd = [i**2 for i in X]
        std_anal = (np.mean(sqrd))**(1/2)
        theoretical_std.append(std_anal)
    
    plt.xlabel("tempo")
    plt.ylabel("x")
    plt.show()
    print("desvio quadratico: ", np.mean(actual_std))
    print("desvio analitico: ", np.mean(theoretical_std))


for step in N:
    walker(step, 0)
    


