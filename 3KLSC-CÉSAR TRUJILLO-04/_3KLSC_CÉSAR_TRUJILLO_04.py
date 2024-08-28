maxf = 3
maxc = 5
a = [[0.0] * maxc for _ in range(maxf)]

for f in range(maxf):
    for c in range(maxc):
        a[f][c] = float(input("Ingresa el elemento en la posicion [" + str(f) + "][" + str(c) + "]: " ))

for f in range(maxf):
    for c in range(maxc):
        print(a[f][c], end = "  ")
    print()
    print()