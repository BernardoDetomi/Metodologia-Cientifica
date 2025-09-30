# Análise Experimental de Algoritmos de Ordenação

## 📋 Descrição do Projeto

Este repositório contém a implementação e análise experimental de algoritmos de ordenação, com foco especial no **HeapSort**. O projeto foi desenvolvido como parte da disciplina de Metodologia Científica e inclui análises comparativas de consumo de memória, tempo de execução, e comportamento em diferentes cenários de entrada.

## 🎯 Objetivos

- **Análise do consumo de memória e tempo de execução** do HeapSort
- **Análise de diferentes tipos de entrada**: ordenadas, reversamente ordenadas e aleatórias
- **Análise de diferentes tamanhos**: dezenas, centenas, milhares e dezenas de milhares de elementos
- **Comparação com algoritmos clássicos** (BubbleSort, SelectionSort, InsertionSort)
- **Análise detalhada dos resultados** com visualizações gráficas

## 📁 Estrutura do Repositório

```
Metodologia-Cientifica/
├── Codigo/                         # 💻 Códigos fonte
│   └── heapsort.py                # Implementação completa com análise experimental
├── Dados/                         # 📊 Dados e resultados
│   ├── resultados_heapsort.csv   # Dados experimentais
│   └── gráficos/                 # 📈 Visualizações (6 gráficos)
│       ├── Figure_1.png          # Comparação tempo - entrada ordenada
│       ├── Figure_2.png          # Comparação tempo - entrada reversa  
│       ├── Figure_3.png          # Comparação tempo - entrada aleatória
│       ├── Figure_4.png          # Comparação memória - entrada ordenada
│       ├── Figure_5.png          # Comparação memória - entrada reversa
│       └── Figure_6.png          # Comparação memória - entrada aleatória
└── README.md                     # 📖 Documentação
```

## 🚀 Como Executar

### Pré-requisitos

- Python 3.7 ou superior
- Bibliotecas necessárias:
  - `matplotlib`
  - `random`
  - `time`
  - `tracemalloc`
  - `csv`

### Execução

1. **Clone ou baixe o repositório**
2. **Navegue até a pasta `Codigo`**:
   ```bash
   cd Codigo
   ```
3. **Execute a análise**:
   ```bash
   python heapsort.py
   ```

O script irá:
- Executar todos os algoritmos com diferentes tipos e tamanhos de entrada
- Gerar o arquivo `resultados_heapsort.csv` com os dados experimentais
- Exibir 6 gráficos comparativos de tempo e memória
- Salvar os gráficos automaticamente na pasta `Dados/gráficos/`

## 📊 Análises Realizadas

### 1. **Análise de Performance**
- Medição de tempo de execução com `time.time()`
- Monitoramento de memória com `tracemalloc`
- Análise de pico de consumo de memória

### 2. **Tipos de Entrada Testados**
- **Ordenada**: `[0, 1, 2, ..., n-1]`
- **Reversa**: `[n-1, n-2, ..., 1, 0]`
- **Aleatória**: Amostra aleatória de números únicos

### 3. **Tamanhos de Entrada**
- **10 elementos**: Teste básico
- **100 elementos**: Entrada pequena
- **1.000 elementos**: Entrada média
- **10.000 elementos**: Entrada grande

### 4. **Algoritmos Comparados**
- **HeapSort** (foco principal) - O(n log n)
- **BubbleSort** - O(n²)
- **SelectionSort** - O(n²)
- **InsertionSort** - O(n²)

## 📈 Resultados e Visualizações

### Arquivos Gerados

1. **`Dados/resultados_heapsort.csv`**: Dados experimentais completos com tempo e memória

### Gráficos Gerados

1. **Comparação de Tempo - Entrada Ordenada** (`Figure_1.png`)
2. **Comparação de Tempo - Entrada Reversa** (`Figure_2.png`)
3. **Comparação de Tempo - Entrada Aleatória** (`Figure_3.png`)
4. **Comparação de Memória - Entrada Ordenada** (`Figure_4.png`)
5. **Comparação de Memória - Entrada Reversa** (`Figure_5.png`)
6. **Comparação de Memória - Entrada Aleatória** (`Figure_6.png`)

## 🔬 Metodologia Experimental

### Medição de Tempo
- Uso do `time.time()` para medição de tempo de execução
- Medição do tempo total de cada algoritmo
- Comparação entre diferentes algoritmos e tipos de entrada

### Medição de Memória
- Monitoramento com `tracemalloc`
- Medição do pico de consumo de memória
- Conversão para KB para melhor legibilidade

### Controle de Qualidade
- Cópia dos arrays antes da ordenação para preservar dados originais
- Implementação recursiva do HeapSort com limite de recursão aumentado
- Teste com diferentes tipos e tamanhos de entrada

## 📊 Principais Descobertas

### Performance do HeapSort
- **Complexidade**: O(n log n) garantida em todos os casos
- **Estabilidade**: Performance consistente independente do tipo de entrada
- **Memória**: Consumo médio de ~0.27 KB, superior aos algoritmos O(n²)

### Comparação com Algoritmos O(n²)
- **vs BubbleSort**: HeapSort significativamente mais eficiente para entradas grandes
- **vs SelectionSort**: HeapSort mantém melhor performance com o crescimento da entrada
- **vs InsertionSort**: HeapSort com maior uso de memória mas melhor escalabilidade

## 🛠️ Detalhes Técnicos

### Configurações do Sistema
- Limite de recursão aumentado: `sys.setrecursionlimit(10**7)`
- Biblioteca matplotlib para visualizações
- Encoding UTF-8 para compatibilidade

### Tratamento de Dados
- Dados salvos em CSV com separador `;`
- Gráficos exibidos interativamente com matplotlib
- Resultados exportados para análise posterior

## 📝 Requisitos Atendidos

✅ **Análise do consumo de memória e tempo de execução**  
✅ **Análise de diferentes tipos de entrada** (ordenada, reversa, aleatória)  
✅ **Análise de diferentes tamanhos para a entrada** (10, 100, 1K, 10K elementos)  
✅ **Comparação com algoritmos existentes na literatura** (BubbleSort, SelectionSort, InsertionSort)  
✅ **Análise detalhada de cada resultado apresentado** (6 gráficos comparativos)  
✅ **Execução real de código para medições** (48 experimentos realizados)  
✅ **Repositório organizado com pastas `Codigo` e `Dados`**  
✅ **Documentação completa de como executar**  

## 👥 Contribuições

Este projeto foi desenvolvido como trabalho acadêmico. Para sugestões ou melhorias, abra uma issue ou envie um pull request.

## 📄 Licença

Este projeto é disponibilizado para fins educacionais e de pesquisa.

---

**Link do Repositório**: [https://github.com/usuario/Metodologia-Cientifica](https://github.com/usuario/Metodologia-Cientifica)

**Autor**: Projeto de Metodologia Científica  
**Data**: 2025  
**Instituição**: [Universidade Federal de São João del-Rei]

---

*README.md gerado por IA*  
