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

## **4. Questão 1.3**

### a) Impacto do Particionamento do Conjunto de Dados A
O particionamento pode acelerar a recuperação e balancear a carga entre os nós quando consultas acessam partes específicas dos dados ou usuários acessam subconjuntos distintos. No entanto, pode aumentar a latência se as consultas exigirem o conjunto inteiro ou elevar custos de sincronização em operações de escrita interdependentes.

### b) Influência do Acesso Desigual ao Conjunto de Dados B
Se B for mais acessado, pode-se replicá-lo em ambos os nós, alocá-lo no nó mais estável ou usar caching para otimizar a resposta e reduzir a sobrecarga.

### c) Impacto de Taxas de Falha no Nó 2
Se o Nó 2 falhar com frequência, é recomendável replicar dados críticos no Nó 1, mover dados menos críticos para o Nó 2 e implementar failover automático para manter a disponibilidade.

### d) Necessidade de Reorganização dos Intervalos de Dados
A reorganização pode ser necessária devido ao crescimento desigual dos dados, mudanças nos padrões de acesso ou falhas frequentes em um nó, visando balanceamento de carga e maior resiliência do sistema.

## **5. Questão 1.4 - Análise de Tempo de Resposta em um Sistema Distribuído Síncrono**

### a) Cálculo do Tempo Total de Resposta com Cache
O tempo total de resposta é afetado pelas seguintes etapas:

1. **Tempo de ida e volta Cliente ⇄ Servidor:**
   - Mínimo: **4 unidades**
   - Máximo: **10 unidades**

2. **Tempo de acesso ao cache:**
   - Mínimo: **0.5 unidade**
   - Máximo: **1 unidade**

3. **Tempo de acesso ao banco de dados (20% das vezes, caso de cache miss):**
   - Mínimo: **11.5 unidades**
   - Máximo: **27.5 unidades**

#### **Melhor caso (100% cache hit)**
- **Tempo total:** **4.5 unidades**

#### **Pior caso (100% cache miss)**
- **Tempo total:** **38.5 unidades**

#### **Tempo médio esperado (80% cache hit, 20% cache miss)**
\[ E[T] = 0.8 \times 4.5 + 0.2 \times 38.5 \]
\[ E[T] = 3.6 + 7.7 = 11.3 \text{ unidades} \]

---

### b) Cálculo do Tempo Total Considerando Falhas de Rede

- **Falha na rede ocorre com 50% de chance.**
- **Se houver falha, o cliente:**
  - Detecta a falha em **2 unidades**
  - Aguarda **5 unidades** antes de tentar novamente

#### **Melhor caso (sem falha de rede)**
- **Tempo total:** **4.5 unidades**

#### **Pior caso (falha na 1ª tentativa, sucesso na 2ª tentativa)**
- **Tempo total:** **45.5 unidades**

#### **Tempo médio esperado (50% falha, 50% sucesso direto)**
\[ E[T] = 0.5 \times 11.3 + 0.5 \times (11.3 + 7) \]
\[ E[T] = 5.65 + 9.15 = 14.8 \text{ unidades} \]

---

## **Resumo Final**

| Cenário | Tempo Total (unidades) |
|--------------------------|----------------------|
| **Melhor caso (100% cache hit, sem falha)** | **4.5** |
| **Pior caso (100% cache miss, falha na 1ª tentativa)** | **45.5** |
| **Tempo médio esperado (80% cache hit, 50% falha)** | **14.8** |

O cache reduz significativamente o tempo médio, mas falhas de rede aumentam bastante o pior caso.


## **6. Questão 1.5**

### a) Por que seria impossível um sistema distribuído oferecer, ao mesmo tempo, consistência (C), disponibilidade (A) e tolerância ao particionamento da rede (P)?
O Teorema CAP afirma que um sistema distribuído pode garantir, no máximo, dois dos três atributos simultaneamente. Isso ocorre porque:

- Se houver particionamento de rede (P), os nós podem ficar temporariamente desconectados.

- Para manter a consistência (C), todas as réplicas precisam estar sincronizadas, o que pode exigir rejeitar algumas requisições até que a conexão seja restabelecida.

- Para garantir disponibilidade (A), o sistema deve sempre responder, mesmo se estiver inconsistente.

- Dessa forma, em presença de uma falha na rede, o sistema deve escolher entre ser consistente (C, rejeitando requisições até sincronizar) ou disponível (A, respondendo com dados possivelmente desatualizados).

### b) Exemplos de sistemas distribuídos compatíveis com as três classes do Teorema CAP
AP (Alta disponibilidade e tolerância a partições, mas sem consistência forte)

- Exemplo: Cassandra (NoSQL)

- Funcionamento: Replica dados em vários nós e responde a consultas mesmo se houver falha na rede, permitindo dados temporariamente inconsistentes.

CP (Consistência forte e tolerância a partições, mas sem alta disponibilidade)

- Exemplo: Zookeeper

- Funcionamento: Prioriza consistência, bloqueando operações de escrita em caso de falha na rede para evitar desatualização de dados.

CA (Consistência e disponibilidade, mas sem tolerância a partições)

- Exemplo: Sistemas de bancos de dados relacionais tradicionais (MySQL, PostgreSQL em modo standalone)

- Funcionamento: Se um nó cair, o sistema não consegue continuar operando, mas garante que todas as operações sejam consistentes e disponíveis dentro de uma única instância.

### c) O Teorema CAP na era da computação em nuvem, contêineres e microsserviços:
O Teorema CAP ainda é relevante, mas sua interpretação mudou com novas tecnologias:

- Computação em nuvem: Serviços distribuídos como AWS DynamoDB utilizam eventual consistency para equilibrar CAP de forma flexível.

- Contêineres e microsserviços: Muitos sistemas adotam AP, priorizando disponibilidade com replicação assíncrona, como ocorre em aplicações baseadas no Apache Kafka.

- Serverless: Plataformas como AWS Lambda e Google Cloud Functions abstraem a complexidade de CAP, mas, internamente, adotam estratégias como sharding e replicação elástica.

Atualmente, a tendência é um trade-off dinâmico entre C, A e P, dependendo da necessidade do serviço.


## **7. Conclusão**

Os cálculos apresentados permitem estimar a disponibilidade de um sistema replicado, fornecendo uma base para projetar infraestruturas tolerantes a falhas. O uso da distribuição binomial evidencia a relação entre redundância e confiabilidade do serviço, sendo um fator crucial na engenharia de sistemas distribuídos.

---

**Referências**\
ASSOCIAÇÃO BRASILEIRA DE NORMAS TÉCNICAS. NBR 14724: Informação e documentação - Trabalhos acadêmicos - Apresentação. ABNT, 2011.\
TANENBAUM, A. S.; VAN STEEN, M. Sistemas Distribuídos: Princípios e Paradigmas. Pearson, 2007.

