# de izquierda a derecha
v = [8, 3, 2, 4, 6, 7, 6]

# for i in range(len(v)):
#     print(v[i])

# de derecha  a izquierda

# for i in range(len(v), 0, -1):
#     print(v[i-1])


# de afuera acia dentro

inicio = 0
fin = len(v)-1


while inicio <= fin:
    print(v[inicio])
    if inicio != fin:
        print(v[fin])
    inicio += 1
    fin -= 1


