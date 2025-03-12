from math import comb

def disponibilidade(n, k, p):
    """
    Calcula a disponibilidade do serviço replicado.
    
    Parâmetros:
    n (int) - Número total de servidores
    k (int) - Mínimo de servidores necessários
    p (float) - Probabilidade de um servidor estar disponível
    
    Retorna:
    float - Probabilidade de o serviço estar disponível
    """
    if k == 1:
        return 1 - (1 - p) ** n
    elif k == n:
        return p ** n
    else:
        return sum(comb(n, i) * (p ** i) * ((1 - p) ** (n - i)) for i in range(k, n + 1))

# Exemplos de uso:
print(disponibilidade(5, 1, 0.9))  # Caso k = 1
print(disponibilidade(5, 5, 0.9))  # Caso k = n
print(disponibilidade(5, 3, 0.9))  # Caso geral
