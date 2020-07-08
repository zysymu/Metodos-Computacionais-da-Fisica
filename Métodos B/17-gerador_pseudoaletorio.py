
#congruente
print("periodo do gerador congruente:")
a = 4
b = 3
M = 100
x_first = 51 #seed, eh o x_1
C = 0 #passos

x = x_first

while True: #loop temporal
    x = (a*x + b)%M
    C += 1
    #print(x)
    if x == x_first:
        print(C)
        break

#schrage
print("periodo do gerador schrage:")
q = 127773
r = 2836
a = 16807
b = 0
M = 2147483544
x_first = 26514
C = 0

x = x_first

#for t in range(100):
while True:
    x = a*(x%q) - r*(x//q)
    if x < 0:
        x = x + M
    #print(x)
    C += 1
    if x == x_first:
        print(C)
        break

    # DEMORA DEMAIS PRA RODAR EM PYTHON!!!
    #decomposicao do M:
    #r = M%a
    #q = M//a
    #M = a*q + r

