"""
Script para comparação detalhada do HeapSort com algoritmos de referência.
Inclui análise de complexidade, casos extremos e performance relativa.
"""

import time
import random
import statistics
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from typing import List, Dict, Callable
import seaborn as sns

class BenchmarkComparison:
    """Classe para comparação detalhada de algoritmos de ordenação"""
    
    def __init__(self):
        self.results = []
        
    def heapsort(self, arr: List[int]) -> List[int]:
        """HeapSort implementation"""
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
                
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        
        n = len(arr)
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
        
        return arr
    
    def quicksort_optimized(self, arr: List[int]) -> List[int]:
        """QuickSort otimizado com mediana de três"""
        def partition(arr, low, high):
            # Mediana de três para escolher pivot
            mid = (low + high) // 2
            if arr[mid] < arr[low]:
                arr[low], arr[mid] = arr[mid], arr[low]
            if arr[high] < arr[low]:
                arr[low], arr[high] = arr[high], arr[low]
            if arr[high] < arr[mid]:
                arr[mid], arr[high] = arr[high], arr[mid]
            
            pivot = arr[high]
            i = low - 1
            
            for j in range(low, high):
                if arr[j] <= pivot:
                    i += 1
                    arr[i], arr[j] = arr[j], arr[i]
            
            arr[i + 1], arr[high] = arr[high], arr[i + 1]
            return i + 1
        
        def quicksort_rec(arr, low, high):
            if low < high:
                pi = partition(arr, low, high)
                quicksort_rec(arr, low, pi - 1)
                quicksort_rec(arr, pi + 1, high)
        
        if len(arr) <= 1:
            return arr
        
        arr_copy = arr.copy()
        quicksort_rec(arr_copy, 0, len(arr_copy) - 1)
        return arr_copy
    
    def mergesort(self, arr: List[int]) -> List[int]:
        """MergeSort implementation"""
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = self.mergesort(arr[:mid])
        right = self.mergesort(arr[mid:])
        
        return self._merge(left, right)
    
    def _merge(self, left: List[int], right: List[int]) -> List[int]:
        """Merge function for MergeSort"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    def generate_test_cases(self) -> Dict[str, Callable]:
        """Gera casos de teste específicos"""
        return {
            "best_case_heap": lambda n: list(range(n)),  # Já ordenado
            "worst_case_heap": lambda n: list(range(n, 0, -1)),  # Ordem reversa
            "average_case": lambda n: random.sample(range(n * 10), n),
            "many_duplicates": lambda n: [random.randint(1, n//10) for _ in range(n)],
            "nearly_sorted": lambda n: self._generate_nearly_sorted(n),
            "few_unique": lambda n: [random.randint(1, 5) for _ in range(n)],
            "alternating": lambda n: [i if i % 2 == 0 else n - i for i in range(n)],
        }
    
    def _generate_nearly_sorted(self, n: int) -> List[int]:
        """Gera array quase ordenado"""
        arr = list(range(n))
        # Fazer algumas trocas aleatórias (5% do tamanho)
        num_swaps = max(1, n // 20)
        for _ in range(num_swaps):
            i, j = random.randint(0, n-1), random.randint(0, n-1)
            arr[i], arr[j] = arr[j], arr[i]
        return arr
    
    def measure_algorithm_performance(self, algorithm: Callable, data: List[int], 
                                    runs: int = 5) -> Dict:
        """Mede performance de um algoritmo com múltiplas execuções"""
        times = []
        
        for _ in range(runs):
            data_copy = data.copy()
            start_time = time.perf_counter()
            
            try:
                result = algorithm(data_copy)
                end_time = time.perf_counter()
                
                # Verificar se está ordenado
                is_sorted = all(result[i] <= result[i+1] for i in range(len(result)-1))
                if not is_sorted:
                    raise ValueError("Resultado não está ordenado")
                
                times.append(end_time - start_time)
                
            except Exception as e:
                print(f"Erro na execução: {e}")
                return {"error": str(e)}
        
        return {
            "mean_time": statistics.mean(times),
            "median_time": statistics.median(times),
            "std_time": statistics.stdev(times) if len(times) > 1 else 0,
            "min_time": min(times),
            "max_time": max(times),
            "runs": runs
        }
    
    def run_comprehensive_benchmark(self):
        """Executa benchmark completo"""
        algorithms = {
            "HeapSort": self.heapsort,
            "QuickSort": self.quicksort_optimized,
            "MergeSort": self.mergesort,
            "TimSort": sorted  # Python's built-in
        }
        
        test_cases = self.generate_test_cases()
        sizes = [100, 500, 1000, 2500, 5000, 10000]
        
        print("🏁 Iniciando benchmark comparativo...")
        print("=" * 60)
        
        for size in sizes:
            print(f"\n📏 Tamanho: {size}")
            
            for case_name, case_generator in test_cases.items():
                print(f"  📋 Caso: {case_name}")
                test_data = case_generator(size)
                
                for alg_name, algorithm in algorithms.items():
                    try:
                        performance = self.measure_algorithm_performance(
                            algorithm, test_data, runs=3
                        )
                        
                        if "error" not in performance:
                            self.results.append({
                                "Algorithm": alg_name,
                                "TestCase": case_name,
                                "Size": size,
                                "MeanTime": performance["mean_time"],
                                "MedianTime": performance["median_time"],
                                "StdTime": performance["std_time"],
                                "MinTime": performance["min_time"],
                                "MaxTime": performance["max_time"]
                            })
                            
                            print(f"    ✅ {alg_name}: {performance['mean_time']:.6f}s "
                                  f"(±{performance['std_time']:.6f})")
                        else:
                            print(f"    ❌ {alg_name}: {performance['error']}")
                            
                    except Exception as e:
                        print(f"    ❌ {alg_name}: Erro - {e}")
        
        print(f"\n✅ Benchmark concluído! {len(self.results)} medições realizadas.")
    
    def analyze_complexity(self):
        """Analisa complexidade empírica dos algoritmos"""
        if not self.results:
            return
        
        df = pd.DataFrame(self.results)
        
        print("\n📊 ANÁLISE DE COMPLEXIDADE EMPÍRICA")
        print("=" * 50)
        
        # Análise por algoritmo
        for algorithm in df['Algorithm'].unique():
            alg_data = df[df['Algorithm'] == algorithm]
            
            print(f"\n🔍 {algorithm}:")
            
            # Calcular fator de crescimento médio
            avg_case_data = alg_data[alg_data['TestCase'] == 'average_case']
            if len(avg_case_data) > 1:
                sizes = sorted(avg_case_data['Size'].unique())
                growth_factors = []
                
                for i in range(1, len(sizes)):
                    prev_size = sizes[i-1]
                    curr_size = sizes[i]
                    
                    prev_time = avg_case_data[avg_case_data['Size'] == prev_size]['MeanTime'].iloc[0]
                    curr_time = avg_case_data[avg_case_data['Size'] == curr_size]['MeanTime'].iloc[0]
                    
                    size_ratio = curr_size / prev_size
                    time_ratio = curr_time / prev_time
                    
                    # Estimar complexidade: O(n^k) -> time_ratio ≈ size_ratio^k
                    if size_ratio > 1 and time_ratio > 0:
                        k = np.log(time_ratio) / np.log(size_ratio)
                        growth_factors.append(k)
                
                if growth_factors:
                    avg_growth = np.mean(growth_factors)
                    print(f"  📈 Fator de crescimento médio: {avg_growth:.2f}")
                    
                    if avg_growth < 1.2:
                        complexity_estimate = "O(n) ou melhor"
                    elif avg_growth < 1.5:
                        complexity_estimate = "O(n log n)"
                    elif avg_growth < 2.2:
                        complexity_estimate = "O(n²)"
                    else:
                        complexity_estimate = "O(n³) ou pior"
                    
                    print(f"  🎯 Complexidade estimada: {complexity_estimate}")
    
    def generate_comparison_plots(self):
        """Gera gráficos de comparação"""
        if not self.results:
            return
        
        df = pd.DataFrame(self.results)
        
        # Criar diretório para gráficos
        import os
        if not os.path.exists("../dados/benchmark"):
            os.makedirs("../dados/benchmark")
        
        # 1. Comparação por caso de teste
        test_cases = df['TestCase'].unique()
        
        for test_case in test_cases:
            plt.figure(figsize=(12, 8))
            case_data = df[df['TestCase'] == test_case]
            
            for algorithm in case_data['Algorithm'].unique():
                alg_data = case_data[case_data['Algorithm'] == algorithm]
                
                # Plot com barras de erro
                plt.errorbar(alg_data['Size'], alg_data['MeanTime'], 
                           yerr=alg_data['StdTime'], 
                           marker='o', label=algorithm, 
                           linewidth=2, markersize=6, capsize=5)
            
            plt.title(f'Comparação de Performance - Caso: {test_case.replace("_", " ").title()}', 
                     fontsize=14, fontweight='bold')
            plt.xlabel('Tamanho da Entrada (n)', fontsize=12)
            plt.ylabel('Tempo Médio (segundos)', fontsize=12)
            plt.legend(fontsize=10)
            plt.grid(True, alpha=0.3)
            plt.yscale('log')
            plt.tight_layout()
            
            plt.savefig(f'../dados/benchmark/comparison_{test_case}.png', 
                       dpi=300, bbox_inches='tight')
            plt.close()
        
        # 2. Heatmap de performance relativa
        pivot_data = df.pivot_table(values='MeanTime', 
                                   index='Algorithm', 
                                   columns='TestCase', 
                                   aggfunc='mean')
        
        plt.figure(figsize=(14, 8))
        sns.heatmap(pivot_data, annot=True, cmap='RdYlGn_r', 
                    fmt='.2e', cbar_kws={'label': 'Tempo Médio (s)'})
        plt.title('Heatmap de Performance - Todos os Casos de Teste', 
                 fontsize=16, fontweight='bold')
        plt.tight_layout()
        
        plt.savefig('../dados/benchmark/performance_heatmap.png', 
                   dpi=300, bbox_inches='tight')
        plt.close()
        
        # 3. Análise específica do HeapSort
        heapsort_data = df[df['Algorithm'] == 'HeapSort']
        
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))
        
        # Tempo médio por caso
        case_means = heapsort_data.groupby('TestCase')['MeanTime'].mean().sort_values()
        ax1.bar(range(len(case_means)), case_means.values, 
                color=plt.cm.viridis(np.linspace(0, 1, len(case_means))))
        ax1.set_xticks(range(len(case_means)))
        ax1.set_xticklabels([case.replace('_', ' ').title() for case in case_means.index], 
                           rotation=45, ha='right')
        ax1.set_ylabel('Tempo Médio (s)')
        ax1.set_title('HeapSort - Performance por Caso de Teste', fontweight='bold')
        ax1.grid(True, alpha=0.3)
        
        # Escalabilidade
        for test_case in ['best_case_heap', 'worst_case_heap', 'average_case']:
            case_data = heapsort_data[heapsort_data['TestCase'] == test_case]
            if not case_data.empty:
                ax2.loglog(case_data['Size'], case_data['MeanTime'], 
                          marker='o', label=test_case.replace('_', ' ').title(), 
                          linewidth=2, markersize=6)
        
        ax2.set_xlabel('Tamanho (n)')
        ax2.set_ylabel('Tempo (s)')
        ax2.set_title('HeapSort - Análise de Escalabilidade', fontweight='bold')
        ax2.legend()
        ax2.grid(True, alpha=0.3)
        
        plt.tight_layout()
        plt.savefig('../dados/benchmark/heapsort_detailed.png', 
                   dpi=300, bbox_inches='tight')
        plt.close()
    
    def save_results(self):
        """Salva resultados do benchmark"""
        if not self.results:
            return
        
        df = pd.DataFrame(self.results)
        
        # Salvar dados brutos
        df.to_csv('../dados/benchmark_results.csv', index=False, sep=';')
        
        # Gerar relatório
        with open('../dados/benchmark_report.txt', 'w', encoding='utf-8') as f:
            f.write("RELATÓRIO DE BENCHMARK - ALGORITMOS DE ORDENAÇÃO\n")
            f.write("=" * 60 + "\n\n")
            
            f.write("RESUMO EXECUTIVO:\n")
            f.write(f"• Total de testes realizados: {len(df)}\n")
            f.write(f"• Algoritmos comparados: {', '.join(df['Algorithm'].unique())}\n")
            f.write(f"• Casos de teste: {len(df['TestCase'].unique())}\n")
            f.write(f"• Tamanhos testados: {sorted(df['Size'].unique())}\n\n")
            
            # Análise por algoritmo
            f.write("ANÁLISE DETALHADA POR ALGORITMO:\n")
            f.write("-" * 40 + "\n")
            
            for algorithm in df['Algorithm'].unique():
                alg_data = df[df['Algorithm'] == algorithm]
                avg_time = alg_data['MeanTime'].mean()
                std_time = alg_data['MeanTime'].std()
                
                f.write(f"\n{algorithm}:\n")
                f.write(f"  • Tempo médio geral: {avg_time:.6f}s (±{std_time:.6f})\n")
                
                # Melhor e pior caso
                best_case = alg_data.loc[alg_data['MeanTime'].idxmin()]
                worst_case = alg_data.loc[alg_data['MeanTime'].idxmax()]
                
                f.write(f"  • Melhor caso: {best_case['TestCase']} "
                       f"({best_case['MeanTime']:.6f}s)\n")
                f.write(f"  • Pior caso: {worst_case['TestCase']} "
                       f"({worst_case['MeanTime']:.6f}s)\n")
        
        print("📊 Resultados do benchmark salvos em:")
        print("   • ../dados/benchmark_results.csv")
        print("   • ../dados/benchmark_report.txt")

def main():
    """Função principal"""
    print("🏆 BENCHMARK COMPARATIVO DE ALGORITMOS DE ORDENAÇÃO")
    print("   Análise Detalhada: HeapSort vs Algoritmos Clássicos")
    print("=" * 60)
    
    benchmark = BenchmarkComparison()
    
    # Executar benchmark
    benchmark.run_comprehensive_benchmark()
    
    # Análise de complexidade
    benchmark.analyze_complexity()
    
    # Gerar gráficos
    print("\n📈 Gerando gráficos comparativos...")
    benchmark.generate_comparison_plots()
    
    # Salvar resultados
    print("\n💾 Salvando resultados...")
    benchmark.save_results()
    
    print("\n✅ Benchmark completo finalizado!")
    print("📁 Verifique a pasta '../dados/benchmark' para os resultados.")

if __name__ == "__main__":
    main()
