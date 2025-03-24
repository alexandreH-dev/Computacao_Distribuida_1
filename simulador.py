import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import comb

def disponibilidade_analitica(n, k, p):
    if k == 1:
        return 1 - (1 - p) ** n
    elif k == n:
        return p ** n
    else:
        return sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k, n + 1))

def simulador_disponibilidade(n, k, p, rodadas):
    # Simulação
    sucesso = 0
    for _ in range(rodadas):
        servidores_disponiveis = np.sum(np.random.rand(n) <= p)
        if servidores_disponiveis >= k:
            sucesso += 1
    freq_experimental = sucesso / rodadas
    
    # Cálculo analítico
    prob_analitica = disponibilidade_analitica(n, k, p)
    
    return freq_experimental, prob_analitica

# Parâmetros de teste
n_vals = [3, 5, 10]
p_vals = [0.5, 0.8]
rodadas = 1

# Coletando resultados
dados = []
for n in n_vals:
    for k in [1, n // 2, n]:
        for p in p_vals:
            freq_exp, prob_analit = simulador_disponibilidade(n, k, p, rodadas)
            dados.append([n, k, p, freq_exp, prob_analit])

df = pd.DataFrame(dados, columns=["n", "k", "p", "Experimental", "Analítico"])
print(df)

# Salvando em CSV para análise
df.to_csv("disponibilidade_resultados.csv", index=False)

# Visualização
for n in n_vals:
    df_n = df[df["n"] == n]
    plt.figure()
    for k in [1, n // 2, n]:
        df_k = df_n[df_n["k"] == k]
        plt.plot(df_k["p"], df_k["Experimental"], marker='o', linestyle='-', label=f'Exp k={k}')
        plt.plot(df_k["p"], df_k["Analítico"], marker='x', linestyle='--', label=f'Analítico k={k}')
    plt.title(f'Disponibilidade para n={n}')
    plt.xlabel('Probabilidade de um servidor estar disponível (p)')
    plt.ylabel('Disponibilidade do serviço')
    plt.legend()
    plt.grid()
    plt.show()