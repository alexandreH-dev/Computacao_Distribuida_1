import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from math import comb

# Função analítica para calcular a disponibilidade
def disponibilidade_analitica(n, k, p):
    if k == 1:
        return 1 - (1 - p) ** n
    elif k == n:
        return p ** n
    else:
        return sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k, n + 1))

# Simulador estocástico
def disponibilidade_estocastica(n, k, p, R):
    sucessos = 0
    for _ in range(R):
        servidores_disponiveis = np.sum(np.random.rand(n) < p)
        if servidores_disponiveis >= k:
            sucessos += 1
    return sucessos / R

# Configurações
n_values = [3, 5, 10]  # Número de servidores
p_values = np.linspace(0, 1, 21)  # Probabilidade de disponibilidade do servidor
R = 100  # Número de rodadas de simulação

# Criar DataFrame para armazenar os resultados
resultados = []

# Rodar simulação para diferentes combinações de n, k e p
for n in n_values:
    for p in p_values:
        for k in [1, n // 2, n]:  # Testando k = 1, n/2, n
            analitico = disponibilidade_analitica(n, k, p)
            estocastico = disponibilidade_estocastica(n, k, p, R)
            resultados.append([n, k, p, analitico, estocastico])

# Converter para DataFrame
df = pd.DataFrame(resultados, columns=["n", "k", "p", "Analítico", "Estocástico"])
print(df.head(10))  # Exibir as primeiras linhas da tabela

# Gerar gráficos
plt.figure(figsize=(12, 6))
for n in n_values:
    for k in [1, n // 2, n]:
        subset = df[(df["n"] == n) & (df["k"] == k)]
        plt.plot(subset["p"], subset["Analítico"], linestyle="dashed", label=f"Teórico n={n}, k={k}")
        plt.scatter(subset["p"], subset["Estocástico"], s=10, label=f"Simulado n={n}, k={k}")

plt.xlabel("Probabilidade p de um servidor estar disponível")
plt.ylabel("Disponibilidade do serviço")
plt.title("Comparação entre valores analíticos e estocásticos")
plt.legend()
plt.grid()
plt.show()

# Salvar os resultados em um arquivo CSV
df.to_csv("comparacao_disponibilidade.csv", index=False)
