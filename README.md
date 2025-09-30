# Análise Experimental de Algoritmos de Ordenação

## 📋 Descrição do Projeto

Este repositório contém a implementação e análise experimental de algoritmos de ordenação, com foco especial no **HeapSort**. O projeto foi desenvolvido como parte da disciplina de Metodologia Científica e inclui análises comparativas de consumo de memória, tempo de execução, e comportamento em diferentes cenários de entrada.

## 🎯 Objetivos

- **Análise do consumo de memória e tempo de execução** do HeapSort
- **Análise de diferentes tipos de entrada**: ordenadas, reversamente ordenadas, desordenadas, parcialmente ordenadas, e com duplicatas
- **Análise de diferentes tamanhos**: dezenas, milhares e milhões de elementos
- **Comparação com algoritmos existentes** na literatura (QuickSort, MergeSort, BubbleSort, etc.)
- **Análise detalhada dos resultados** com visualizações e relatórios estatísticos

## 📁 Estrutura do Repositório

```
metodologia/
├── codigo/                          # 💻 Códigos fonte
│   ├── heapsort_analysis.py        # Análise experimental completa
│   ├── benchmark_comparison.py     # Comparação detalhada entre algoritmos
│   ├── run_analysis.py            # Script principal de execução
│   └── heapsort_original.py       # Implementação original do HeapSort
├── dados/                          # 📊 Dados e resultados
│   ├── resultados_completos.csv   # Dados experimentais principais
│   ├── benchmark_results.csv      # Resultados do benchmark
│   ├── relatorio_estatistico.txt  # Análise estatística
│   ├── benchmark_report.txt       # Relatório do benchmark
│   ├── graficos/                  # 📈 Visualizações principais
│   └── benchmark/                 # 🏆 Gráficos de comparação
└── README.md                      # 📖 Documentação
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas necessárias (instaladas automaticamente):
  - `matplotlib`
  - `pandas`
  - `numpy`
  - `seaborn`

### Execução Completa

1. **Clone ou baixe o repositório**
2. **Navegue até a pasta `codigo`**:
   ```bash
   cd codigo
   ```
3. **Execute a análise completa**:
   ```bash
   python run_analysis.py
   ```

### Execuções Específicas

Para executar apenas análises específicas:

```bash
# Análise experimental principal
python heapsort_analysis.py

# Benchmark comparativo detalhado
python benchmark_comparison.py
```

## 📊 Análises Realizadas

### 1. **Análise de Performance**
- Medição de tempo de execução com `time.perf_counter()`
- Monitoramento de memória com `tracemalloc`
- Múltiplas execuções para cálculo de estatísticas

### 2. **Tipos de Entrada Testados**
- **Ordenada**: `[1, 2, 3, ..., n]`
- **Reversa**: `[n, n-1, ..., 2, 1]`
- **Aleatória**: Permutação aleatória
- **Parcialmente Ordenada**: 90% ordenada com 10% de elementos fora de lugar
- **Muitas Duplicatas**: Apenas 10% de valores únicos
- **Poucos Valores Únicos**: Máximo de 5 valores diferentes
- **Alternada**: Padrão alternado de valores

### 3. **Tamanhos de Entrada**
- **Pequenos**: 10, 50, 100 elementos
- **Médios**: 500, 1.000, 5.000 elementos  
- **Grandes**: 10.000+ elementos (conforme capacidade)

### 4. **Algoritmos Comparados**
- **HeapSort** (foco principal)
- **QuickSort** (otimizado com mediana de três)
- **MergeSort**
- **TimSort** (algoritmo nativo do Python)
- **BubbleSort** (referência O(n²))
- **SelectionSort** (referência O(n²))
- **InsertionSort** (referência O(n²))

## 📈 Resultados e Visualizações

### Arquivos Gerados

1. **`dados/resultados_completos.csv`**: Dados experimentais completos
2. **`dados/benchmark_results.csv`**: Resultados do benchmark comparativo
3. **`dados/relatorio_estatistico.txt`**: Análise estatística detalhada
4. **`dados/benchmark_report.txt`**: Relatório de performance

### Gráficos Gerados

1. **Comparação de Tempo por Tipo de Entrada**
2. **Análise de Consumo de Memória**
3. **Análise de Escalabilidade**
4. **Heatmap de Performance**
5. **Análise Específica do HeapSort**
6. **Gráficos de Benchmark Comparativo**

## 🔬 Metodologia Experimental

### Medição de Tempo
- Uso do `time.perf_counter()` para alta precisão
- Múltiplas execuções (3-5 repetições) para cálculo de estatísticas
- Cálculo de média, mediana, desvio padrão, mínimo e máximo

### Medição de Memória
- Monitoramento com `tracemalloc`
- Medição do pico de consumo de memória
- Conversão para KB para melhor legibilidade

### Controle de Qualidade
- Verificação automática de corretude (array ordenado)
- Tratamento de exceções e timeouts
- Validação de entrada e saída

## 📊 Principais Descobertas

### Performance do HeapSort
- **Complexidade**: O(n log n) garantida em todos os casos
- **Estabilidade**: Performance consistente independente do tipo de entrada
- **Memória**: Ordenação in-place com baixo overhead de memória

### Comparação com Outros Algoritmos
- **vs QuickSort**: Mais estável, mas ligeiramente mais lento no caso médio
- **vs MergeSort**: Menor uso de memória, performance similar
- **vs Algoritmos O(n²)**: Significativamente superior para entradas grandes

## 🛠️ Detalhes Técnicos

### Configurações do Sistema
- Limite de recursão aumentado: `sys.setrecursionlimit(10**7)`
- Estilo de gráficos: `seaborn-v0_8`
- Encoding: UTF-8 para compatibilidade

### Tratamento de Dados
- Dados salvos em CSV com separador `;`
- Gráficos salvos em PNG com alta resolução (300 DPI)
- Relatórios em texto plano UTF-8

## 📝 Requisitos Atendidos

✅ **Análise do consumo de memória e tempo de execução**  
✅ **Análise de diferentes tipos de entrada**  
✅ **Análise de diferentes tamanhos para a entrada**  
✅ **Comparação com algoritmos existentes na literatura**  
✅ **Análise detalhada de cada resultado apresentado**  
✅ **Execução real de código para medições**  
✅ **Repositório organizado com pastas `codigo` e `dados`**  
✅ **Documentação completa de como executar**  

## 👥 Contribuições

Este projeto foi desenvolvido como trabalho acadêmico. Para sugestões ou melhorias, abra uma issue ou envie um pull request.

## 📄 Licença

Este projeto é disponibilizado para fins educacionais e de pesquisa.

---

**Link do Repositório**: [https://github.com/usuario/metodologia-algoritmos](https://github.com/usuario/metodologia-algoritmos)

**Autor**: Projeto de Metodologia Científica  
**Data**: 2024  
**Instituição**: [Nome da Instituição]
