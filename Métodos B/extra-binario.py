def binint(n):
    if 0 < n < 255:
        a = []
        for v in range(8):
            a.append(n%2)
            n = n//2 #divisao por inteiros
        return a
        

    else:
        print("entre um valor entre 0 e 255")

a = binint(4)
[print(i, end='') for i in a[::-1]]

x=0
for v in range(8):
    x += a[v] * 2**v
print("fazendo a prova real: ", x)
    
