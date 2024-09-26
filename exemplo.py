n = 4  # Número de homens e mulheres

wmr = [
    [1, 2, 0, 3],  # Homem 1
    [0, 1, 3, 2],  # Homem 2
    [2, 3, 1, 0],  # Homem 3
    [0, 2, 1, 3]   # Homem 4
]

mwr = [
    [2, 0, 1, 3],  # Mulher 1
    [1, 3, 0, 2],  # Mulher 2
    [3, 0, 2, 1],  # Mulher 3
    [0, 2, 3, 1]   # Mulher 4
]

rmw = [[0] * n for _ in range(n)]  # Rank das mulheres para os homens
rwm = [[0] * n for _ in range(n)]  # Rank dos homens para as mulheres
x = [-1] * n  # Casamento dos homens
y = [-1] * n  # Casamento das mulheres
single = [True] * n  # Estado de solteira das mulheres

def print_result():
    rm = 0
    rw = 0
    for m in range(n):
        print(f"Homem {m + 1} casado com Mulher {x[m] + 1}")
        rm += rmw[m][x[m]]
        rw += rwm[x[m]][m]
    print(f"Rank total dos homens: {rm}, Rank total das mulheres: {rw}")

def stable(m, w, r):
    s = True
    i = 1
    while i < r and s:
        pw = wmr[m][i - 1]
        i += 1
        if not single[pw]:
            if rwm[pw][m] > rwm[pw][y[pw]]:
                s = False

    i = 1
    lim = rwm[w][m]
    while i < lim and s:
        pm = mwr[w][i - 1]
        i += 1
        if pm < m:
            if rmw[pm][w] > rmw[pm][x[pm]]:
                s = False

    return s

def try_match(m):
    for r in range(n):
        w = wmr[m][r]
        if single[w]:
            if stable(m, w, r):
                x[m] = w
                y[w] = m
                single[w] = False
                if m < n - 1:
                    try_match(m + 1)
                else:
                    print_result()
                single[w] = True

# Preencher os rankings baseados nas preferências
for m in range(n):
    for r in range(n):
        rmw[m][wmr[m][r]] = r

for w in range(n):
    for r in range(n):
        rwm[w][mwr[w][r]] = r

# Inicializar o processo de casamento
try_match(0)
