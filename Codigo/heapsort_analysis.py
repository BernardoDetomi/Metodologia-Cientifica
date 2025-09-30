import random
import time
import tracemalloc
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import sys
import csv
import os
from typing import List, Callable, Dict, Tuple
import seaborn as sns

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

sys.setrecursionlimit(10**7)

class SortingAnalyzer:
    """Classe para análise experimental de algoritmos de ordenação"""
    
    def __init__(self):
        self.results = []
        self.algorithms = {
            "HeapSort": self.heapsort,
            "QuickSort": self.quicksort,
            "MergeSort": self.mergesort,
            "BubbleSort": self.bubble_sort,
            "SelectionSort": self.selection_sort,
            "InsertionSort": self.insertion_sort,
            "TimSort": sorted  # Algoritmo nativo do Python
        }
    
    def heapsort(self, arr: List[int]) -> List[int]:
        """Implementação do HeapSort"""
        def heapify(arr, n, i):
            maior = i
            esquerda = 2 * i + 1
            direita = 2 * i + 2

            if esquerda < n and arr[esquerda] > arr[maior]:
                maior = esquerda
            if direita < n and arr[direita] > arr[maior]:
                maior = direita

            if maior != i:
                arr[i], arr[maior] = arr[maior], arr[i]
                heapify(arr, n, maior)

        n = len(arr)
        # Construir heap máximo
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)

        # Extrair elementos do heap um por um
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)

        return arr
    
    def quicksort(self, arr: List[int]) -> List[int]:
        """Implementação do QuickSort"""
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        esquerda = [x for x in arr if x < pivot]
        meio = [x for x in arr if x == pivot]
        direita = [x for x in arr if x > pivot]
        
        return self.quicksort(esquerda) + meio + self.quicksort(direita)
    
    def mergesort(self, arr: List[int]) -> List[int]:
        """Implementação do MergeSort"""
        if len(arr) <= 1:
            return arr
        
        meio = len(arr) // 2
        esquerda = self.mergesort(arr[:meio])
        direita = self.mergesort(arr[meio:])
        
        return self._merge(esquerda, direita)
    
    def _merge(self, esquerda: List[int], direita: List[int]) -> List[int]:
        """Função auxiliar para merge"""
        resultado = []
        i = j = 0
        
        while i < len(esquerda) and j < len(direita):
            if esquerda[i] <= direita[j]:
                resultado.append(esquerda[i])
                i += 1
            else:
                resultado.append(direita[j])
                j += 1
        
        resultado.extend(esquerda[i:])
        resultado.extend(direita[j:])
        return resultado
    
    def bubble_sort(self, arr: List[int]) -> List[int]:
        """Implementação do BubbleSort"""
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return arr
    
    def selection_sort(self, arr: List[int]) -> List[int]:
        """Implementação do SelectionSort"""
        n = len(arr)
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]
        return arr
    
    def insertion_sort(self, arr: List[int]) -> List[int]:
        """Implementação do InsertionSort"""
        for i in range(1, len(arr)):
            chave = arr[i]
            j = i - 1
            while j >= 0 and chave < arr[j]:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = chave
        return arr
    
    def measure_performance(self, algorithm: Callable, arr: List[int]) -> Tuple[float, float, bool]:
        """Mede tempo de execução e consumo de memória de um algoritmo"""
        arr_copy = arr.copy()
        
        # Iniciar monitoramento de memória
        tracemalloc.start()
        
        # Medir tempo
        start_time = time.perf_counter()
        
        try:
            algorithm(arr_copy)
            success = True
        except Exception as e:
            print(f"Erro na execução: {e}")
            success = False
        
        end_time = time.perf_counter()
        
        # Obter informações de memória
        current_memory, peak_memory = tracemalloc.get_traced_memory()
        tracemalloc.stop()
        
        execution_time = end_time - start_time
        memory_usage = peak_memory / 1024  # Converter para KB
        
        return execution_time, memory_usage, success
    
    def generate_test_data(self, size: int) -> Dict[str, List[int]]:
        """Gera diferentes tipos de entrada para teste"""
        return {
            "ordenada": list(range(size)),
            "reversa": list(range(size, 0, -1)),
            "aleatoria": random.sample(range(size * 10), size),
            "parcialmente_ordenada": self._generate_partially_sorted(size),
            "muitas_duplicatas": self._generate_with_duplicates(size)
        }
    
    def _generate_partially_sorted(self, size: int) -> List[int]:
        """Gera array parcialmente ordenado (90% ordenado)"""
        arr = list(range(size))
        # Embaralhar apenas 10% dos elementos
        num_swaps = size // 10
        for _ in range(num_swaps):
            i, j = random.randint(0, size-1), random.randint(0, size-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    def _generate_with_duplicates(self, size: int) -> List[int]:
        """Gera array com muitas duplicatas"""
        unique_values = size // 10  # 10% de valores únicos
        return [random.randint(0, unique_values) for _ in range(size)]
    
    def run_comprehensive_analysis(self):
        """Executa análise completa dos algoritmos"""
        # Diferentes tamanhos de entrada
        sizes = [10, 50, 100, 500, 1000, 5000, 10000]
        
        # Para algoritmos mais lentos, limitar o tamanho
        slow_algorithms = ["BubbleSort", "SelectionSort", "InsertionSort"]
        
        print("🔍 Iniciando análise experimental completa...")
        print("=" * 60)
        
        for size in sizes:
            print(f"\n📊 Analisando tamanho: {size}")
            test_data = self.generate_test_data(size)
            
            for input_type, data in test_data.items():
                print(f"  📋 Tipo de entrada: {input_type}")
                
                for alg_name, algorithm in self.algorithms.items():
                    # Pular algoritmos lentos para tamanhos grandes
                    if size > 1000 and alg_name in slow_algorithms:
                        continue
                    
                    try:
                        exec_time, memory, success = self.measure_performance(algorithm, data)
                        
                        if success:
                            self.results.append({
                                "Algoritmo": alg_name,
                                "TipoEntrada": input_type,
                                "Tamanho": size,
                                "TempoSegundos": exec_time,
                                "MemoriaKB": memory,
                                "ComplexidadeTeorica": self._get_complexity(alg_name),
                                "Sucesso": True
                            })
                            print(f"    ✅ {alg_name}: {exec_time:.6f}s, {memory:.2f}KB")
                        else:
                            print(f"    ❌ {alg_name}: Falha na execução")
                            
                    except Exception as e:
                        print(f"    ❌ {alg_name}: Erro - {e}")
        
        print(f"\n✅ Análise concluída! {len(self.results)} medições realizadas.")
    
    def _get_complexity(self, algorithm_name: str) -> str:
        """Retorna a complexidade teórica do algoritmo"""
        complexities = {
            "HeapSort": "O(n log n)",
            "QuickSort": "O(n log n) médio, O(n²) pior",
            "MergeSort": "O(n log n)",
            "BubbleSort": "O(n²)",
            "SelectionSort": "O(n²)",
            "InsertionSort": "O(n²)",
            "TimSort": "O(n log n)"
        }
        return complexities.get(algorithm_name, "N/A")
    
    def save_results(self, filename: str = "resultados_completos.csv"):
        """Salva os resultados em arquivo CSV"""
        if not os.path.exists("../dados"):
            os.makedirs("../dados")
        
        filepath = os.path.join("../dados", filename)
        
        df = pd.DataFrame(self.results)
        df.to_csv(filepath, index=False, sep=';', encoding='utf-8')
        
        print(f"📁 Resultados salvos em: {filepath}")
        return filepath
    
    def generate_visualizations(self):
        """Gera visualizações dos resultados"""
        if not self.results:
            print("❌ Nenhum resultado disponível para visualização")
            return
        
        df = pd.DataFrame(self.results)
        
        # Criar diretório para gráficos
        if not os.path.exists("../dados/graficos"):
            os.makedirs("../dados/graficos")
        
        # 1. Comparação de tempo por tipo de entrada
        self._plot_time_comparison(df)
        
        # 2. Comparação de memória
        self._plot_memory_comparison(df)
        
        # 3. Análise de escalabilidade
        self._plot_scalability_analysis(df)
        
        # 4. Heatmap de performance
        self._plot_performance_heatmap(df)
        
        # 5. Análise específica do HeapSort
        self._plot_heapsort_analysis(df)
    
    def _plot_time_comparison(self, df: pd.DataFrame):
        """Gráfico de comparação de tempo"""
        input_types = df['TipoEntrada'].unique()
        
        for input_type in input_types:
            plt.figure(figsize=(12, 8))
            
            subset = df[df['TipoEntrada'] == input_type]
            
            for algorithm in subset['Algoritmo'].unique():
                alg_data = subset[subset['Algoritmo'] == algorithm]
                plt.loglog(alg_data['Tamanho'], alg_data['TempoSegundos'], 
                          marker='o', label=algorithm, linewidth=2, markersize=6)
            
            plt.title(f'Comparação de Tempo de Execução - Entrada {input_type.title()}', 
                     fontsize=16, fontweight='bold')
            plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
            plt.ylabel('Tempo de Execução (segundos)', fontsize=12)
            plt.legend(fontsize=10)
            plt.grid(True, alpha=0.3)
            plt.tight_layout()
            
            plt.savefig(f'../dados/graficos/tempo_{input_type}.png', dpi=300, bbox_inches='tight')
            plt.close()
    
    def _plot_memory_comparison(self, df: pd.DataFrame):
        """Gráfico de comparação de memória"""
        plt.figure(figsize=(12, 8))
        
        # Agrupar por algoritmo e calcular média de memória
        memory_avg = df.groupby(['Algoritmo', 'Tamanho'])['MemoriaKB'].mean().reset_index()
        
        for algorithm in memory_avg['Algoritmo'].unique():
            alg_data = memory_avg[memory_avg['Algoritmo'] == algorithm]
            plt.plot(alg_data['Tamanho'], alg_data['MemoriaKB'], 
                    marker='s', label=algorithm, linewidth=2, markersize=6)
        
        plt.title('Comparação de Consumo de Memória', fontsize=16, fontweight='bold')
        plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
        plt.ylabel('Consumo de Memória (KB)', fontsize=12)
        plt.legend(fontsize=10)
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        plt.savefig('../dados/graficos/memoria_comparacao.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _plot_scalability_analysis(self, df: pd.DataFrame):
        """Análise de escalabilidade"""
        fig, axes = plt.subplots(2, 2, figsize=(15, 12))
        fig.suptitle('Análise de Escalabilidade dos Algoritmos', fontsize=16, fontweight='bold')
        
        algorithms = ['HeapSort', 'QuickSort', 'MergeSort', 'TimSort']
        
        for i, algorithm in enumerate(algorithms):
            ax = axes[i//2, i%2]
            alg_data = df[df['Algoritmo'] == algorithm]
            
            for input_type in alg_data['TipoEntrada'].unique():
                type_data = alg_data[alg_data['TipoEntrada'] == input_type]
                ax.loglog(type_data['Tamanho'], type_data['TempoSegundos'], 
                         marker='o', label=input_type, linewidth=2)
            
            ax.set_title(f'{algorithm}', fontweight='bold')
            ax.set_xlabel('Tamanho (n)')
            ax.set_ylabel('Tempo (s)')
            ax.legend(fontsize=8)
            ax.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('../dados/graficos/escalabilidade.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _plot_performance_heatmap(self, df: pd.DataFrame):
        """Heatmap de performance"""
        # Criar pivot table para o heatmap
        pivot_time = df.pivot_table(values='TempoSegundos', 
                                   index='Algoritmo', 
                                   columns='TipoEntrada', 
                                   aggfunc='mean')
        
        plt.figure(figsize=(10, 8))
        sns.heatmap(pivot_time, annot=True, cmap='YlOrRd', fmt='.2e', 
                    cbar_kws={'label': 'Tempo Médio (s)'})
        plt.title('Heatmap de Performance - Tempo de Execução', 
                 fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        plt.savefig('../dados/graficos/heatmap_performance.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def _plot_heapsort_analysis(self, df: pd.DataFrame):
        """Análise específica do HeapSort"""
        heapsort_data = df[df['Algoritmo'] == 'HeapSort']
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))
        
        # Gráfico 1: Tempo vs Tamanho
        for input_type in heapsort_data['TipoEntrada'].unique():
            type_data = heapsort_data[heapsort_data['TipoEntrada'] == input_type]
            ax1.loglog(type_data['Tamanho'], type_data['TempoSegundos'], 
                      marker='o', label=input_type, linewidth=2, markersize=6)
        
        ax1.set_title('HeapSort - Tempo de Execução', fontweight='bold')
        ax1.set_xlabel('Tamanho da Entrada (n)')
        ax1.set_ylabel('Tempo (segundos)')
        ax1.legend()
        ax1.grid(True, alpha=0.3)
        
        # Gráfico 2: Memória vs Tamanho
        for input_type in heapsort_data['TipoEntrada'].unique():
            type_data = heapsort_data[heapsort_data['TipoEntrada'] == input_type]
            ax2.plot(type_data['Tamanho'], type_data['MemoriaKB'], 
                    marker='s', label=input_type, linewidth=2, markersize=6)
        
        ax2.set_title('HeapSort - Consumo de Memória', fontweight='bold')
        ax2.set_xlabel('Tamanho da Entrada (n)')
        ax2.set_ylabel('Memória (KB)')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('../dados/graficos/heapsort_analise.png', dpi=300, bbox_inches='tight')
        plt.close()
    
    def generate_statistical_analysis(self):
        """Gera análise estatística dos resultados"""
        if not self.results:
            return
        
        df = pd.DataFrame(self.results)
        
        # Relatório estatístico
        report = []
        report.append("=" * 80)
        report.append("RELATÓRIO ESTATÍSTICO - ANÁLISE DE ALGORITMOS DE ORDENAÇÃO")
        report.append("=" * 80)
        report.append("")
        
        # Estatísticas gerais
        report.append("📊 ESTATÍSTICAS GERAIS:")
        report.append(f"   • Total de execuções: {len(df)}")
        report.append(f"   • Algoritmos analisados: {len(df['Algoritmo'].unique())}")
        report.append(f"   • Tipos de entrada: {len(df['TipoEntrada'].unique())}")
        report.append(f"   • Tamanhos testados: {sorted(df['Tamanho'].unique())}")
        report.append("")
        
        # Análise por algoritmo
        report.append("🔍 ANÁLISE POR ALGORITMO:")
        for algorithm in df['Algoritmo'].unique():
            alg_data = df[df['Algoritmo'] == algorithm]
            avg_time = alg_data['TempoSegundos'].mean()
            avg_memory = alg_data['MemoriaKB'].mean()
            complexity = self._get_complexity(algorithm)
            
            report.append(f"   • {algorithm}:")
            report.append(f"     - Tempo médio: {avg_time:.6f}s")
            report.append(f"     - Memória média: {avg_memory:.2f}KB")
            report.append(f"     - Complexidade: {complexity}")
            report.append("")
        
        # Salvar relatório
        with open("../dados/relatorio_estatistico.txt", "w", encoding="utf-8") as f:
            f.write("\n".join(report))
        
        print("📄 Relatório estatístico salvo em: ../dados/relatorio_estatistico.txt")

def main():
    """Função principal"""
    print("🚀 Iniciando Análise Experimental de Algoritmos de Ordenação")
    print("=" * 60)
    
    analyzer = SortingAnalyzer()
    
    # Executar análise completa
    analyzer.run_comprehensive_analysis()
    
    # Salvar resultados
    analyzer.save_results()
    
    # Gerar visualizações
    print("\n📈 Gerando visualizações...")
    analyzer.generate_visualizations()
    
    # Gerar análise estatística
    print("\n📊 Gerando análise estatística...")
    analyzer.generate_statistical_analysis()
    
    print("\n✅ Análise completa finalizada!")
    print("📁 Verifique a pasta '../dados' para os resultados e gráficos.")

if __name__ == "__main__":
    main()
