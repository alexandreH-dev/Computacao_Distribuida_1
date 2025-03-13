**UNIVERSIDADE DE FORTALEZA**\
Departamento de Computação

**EXERCÍCIO 1.1**

**Membros:** Alexandre Henrique, Antônio Alves e Renan Almeida

---

# **Disponibilidade de um Serviço Replicado em Múltiplos Servidores**

## **1. Introdução**

A disponibilidade de serviços é um fator essencial na computação distribuída. Em sistemas replicados, servidores redundantes garantem continuidade mesmo diante de falhas. Este estudo visa deduzir uma fórmula matemática para calcular a disponibilidade de um serviço replicado em múltiplos servidores, considerando diferentes critérios de acesso e número mínimo de servidores operacionais.

## **2. Definição do Problema**

Seja um sistema com os seguintes parâmetros:

- **n**: Número total de servidores (÷ n > 0)
- **k**: Número mínimo de servidores necessários para o funcionamento (0 < k ≤ n)
- **p**: Probabilidade de cada servidor estar disponível em um dado instante (0 ≤ p ≤ 1)

Nosso objetivo é calcular a disponibilidade \(A(n, k, p)\), ou seja, a probabilidade do serviço estar acessível.

## **3. Derivação Matemática**

O serviço estará disponível se pelo menos um servidor estiver operacional. A forma mais simples de calcular essa probabilidade é considerar o evento complementar, ou seja, a falha de todos os servidores simultaneamente:

$$
A(n,1,p) = 1 - (1 - p)^n
$$

Aqui, todos os servidores devem estar disponíveis para que o serviço funcione. Como cada servidor tem probabilidade \(p\) de estar ativo, e eles são independentes, temos:

$$
A(n,n,p) = p^n
$$

Neste caso, o serviço estará disponível se pelo menos \(k\) servidores estiverem operacionais. Modelamos esse problema como uma distribuição binomial:

$$
A(n,k,p) = \sum_{i=k}^{n} \binom{n}{i} p^i (1 - p)^{(n-i)}
$$

Essa equação representa a soma das probabilidades de termos exatamente \(k\), \(k+1\), ..., até \(n\) servidores disponíveis.

## **4. Conclusão**

Os cálculos apresentados permitem estimar a disponibilidade de um sistema replicado, fornecendo uma base para projetar infraestruturas tolerantes a falhas. O uso da distribuição binomial evidencia a relação entre redundância e confiabilidade do serviço, sendo um fator crucial na engenharia de sistemas distribuídos.

---

**Referências**\
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 14724: Informação e documentação - Trabalhos acadêmicos - Apresentação. ABNT, 2011.\
TANENBAUM, A. S.; VAN STEEN, M. Sistemas Distribuídos: Princípios e Paradigmas. Pearson, 2007.

