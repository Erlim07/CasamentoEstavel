# Problema dos casamentos estáveis
n = 8  # Número de homens e mulheres

# Definindo os tipos e arrays
wmr = [[0] * n for _ in range(n)]  # wmr[man][rank]: a mulher que o homem 'man' prefere na posição 'rank'
mwr = [[0] * n for _ in range(n)]  # mwr[woman][rank]: o homem que a mulher 'woman' prefere na posição 'rank'
rmw = [[0] * n for _ in range(n)]  # rmw[man][woman]: o rank da mulher para o homem
rwm = [[0] * n for _ in range(n)]  # rwm[woman][man]: o rank do homem para a mulher
x = [-1] * n  # x[man]: a mulher casada com o homem 'man'
y = [-1] * n  # y[woman]: o homem casado com a mulher 'woman'
single = [True] * n  # single[woman]: indica se a mulher está solteira

def print_result():
    rm = 0
    rw = 0
    for m in range(n):
        print(f"{x[m]:4}", end=" ")
        rm += rmw[m][x[m]]
        rw += rwm[x[m]][m]
    print(f"{rm:8} {rw:4}")

def stable(m, w, r):
    s = True
    i = 1
    # Verifica se a mulher 'w' é uma escolha estável para o homem 'm'
    
    # Primeiro loop para verificar se 'm' tem uma preferência mais alta disponível
    while i < r and s:
        pw = wmr[m][i - 1]
        i += 1
        if not single[pw]:
            if rwm[pw][m] > rwm[pw][y[pw]]:
                s = False

    # Segundo loop para verificar se 'w' tem um homem que ela prefira mais do que 'm'
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

# Programa principal
if __name__ == "__main__":
    # Leitura das preferências dos homens
    for m in range(n):
        for r in range(n):
            wmr[m][r] = int(input(f"Digite a {r + 1}ª preferência da mulher para o homem {m + 1}: ")) - 1
            rmw[m][wmr[m][r]] = r

    # Leitura das preferências das mulheres
    for w in range(n):
        for r in range(n):
            mwr[w][r] = int(input(f"Digite a {r + 1}ª preferência do homem para a mulher {w + 1}: ")) - 1
            rwm[w][mwr[w][r]] = r

    # Inicializar todas as mulheres como solteiras
    for w in range(n):
        single[w] = True

    # Iniciar a tentativa de casamento a partir do primeiro homem
    try_match(0)
