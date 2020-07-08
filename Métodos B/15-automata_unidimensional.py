import random

def binint(n):
    if 0 < n < 255:
        a = []
        for v in range(8):
            a.append(n%2)
            n = n//2 #divisao por inteiros
        return a[::-1]

def p(ol):
    for el in ol:
        if el == 0:
            print(' ', end='')
        else:
            print('$', end='')
    print("\n")

#entrada
r = int(input("regra (numero entre 0 e 255) : "))
if r<0 or r>255:
    raise TypeError("so pode entre 0 e 255")

n = int(input("tamanho do automata: ")) #tamanho do array
seed = random.randint(0,1) #a seed so pode ser 0 ou 1

ac = [0]*n #automata celular
c = [0]*n #novo objeto criado a partir do ac


#estado inicial
for i in range(n):
    if seed == 0:
        ac[i] = 0
        ac[n//2] = 1

    else:
        ac[i] = random.randint(0,1)


#obtencao da regra
f = binint(r)

#dinamica do ac
for t in range(n): #laco temporal
    for j in range(1, n-2):
        v = ac[j-1]*4 + ac[j]*2 + ac[j+1]
        c[j] = f[v]

    #condicoes de contorno
    v = ac[n-1]*4 + ac[0]*2 + ac[1]
    c[0] = f[v]
    v = ac[n-2]*4 + ac[n-1]*2 + ac[0]
    c[n-1] = f[v]

    p(c)
    ac = c


