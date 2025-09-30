#!/usr/bin/env python3
"""
Script principal para executar a análise experimental completa
dos algoritmos de ordenação, incluindo HeapSort.

Este script executa todas as análises necessárias e gera os resultados
na pasta 'dados/' conforme especificado nos requisitos do projeto.
"""

import os
import sys
import subprocess
import time
from pathlib import Path

def ensure_dependencies():
    """Verifica e instala dependências necessárias"""
    required_packages = [
        'matplotlib',
        'pandas',
        'numpy',
        'seaborn'
    ]
    
    print("🔍 Verificando dependências...")
    
    for package in required_packages:
        try:
            __import__(package)
            print(f"  ✅ {package}")
        except ImportError:
            print(f"  ❌ {package} não encontrado. Instalando...")
            try:
                subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
                print(f"  ✅ {package} instalado com sucesso")
            except subprocess.CalledProcessError:
                print(f"  ❌ Erro ao instalar {package}")
                return False
    
    return True

def create_directories():
    """Cria as estruturas de diretório necessárias"""
    directories = [
        "../dados",
        "../dados/graficos",
        "../dados/raw_data"
    ]
    
    for directory in directories:
        Path(directory).mkdir(parents=True, exist_ok=True)
        print(f"📁 Diretório criado/verificado: {directory}")

def run_analysis():
    """Executa a análise principal"""
    print("\n" + "="*60)
    print("🚀 INICIANDO ANÁLISE EXPERIMENTAL")
    print("="*60)
    
    start_time = time.time()
    
    try:
        # Importar e executar análise
        from heapsort_analysis import SortingAnalyzer
        
        analyzer = SortingAnalyzer()
        
        # Executar análise completa
        print("📊 Executando análise experimental...")
        analyzer.run_comprehensive_analysis()
        
        # Salvar resultados
        print("💾 Salvando resultados...")
        analyzer.save_results()
        
        # Gerar visualizações
        print("📈 Gerando visualizações...")
        analyzer.generate_visualizations()
        
        # Gerar análise estatística
        print("📊 Gerando análise estatística...")
        analyzer.generate_statistical_analysis()
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        print("\n" + "="*60)
        print("✅ ANÁLISE CONCLUÍDA COM SUCESSO!")
        print(f"⏱️  Tempo total de execução: {execution_time:.2f} segundos")
        print("="*60)
        
        print("\n📁 ARQUIVOS GERADOS:")
        print("   • ../dados/resultados_completos.csv - Dados experimentais")
        print("   • ../dados/relatorio_estatistico.txt - Análise estatística")
        print("   • ../dados/graficos/ - Visualizações e gráficos")
        
        return True
        
    except Exception as e:
        print(f"\n❌ ERRO durante a execução: {e}")
        import traceback
        traceback.print_exc()
        return False

def main():
    """Função principal"""
    print("🔬 ANÁLISE EXPERIMENTAL DE ALGORITMOS DE ORDENAÇÃO")
    print("   Projeto de Metodologia Científica")
    print("   Foco: HeapSort vs Algoritmos Clássicos")
    print("")
    
    # Verificar dependências
    if not ensure_dependencies():
        print("❌ Erro nas dependências. Abortando.")
        return 1
    
    # Criar diretórios
    create_directories()
    
    # Executar análise
    success = run_analysis()
    
    if success:
        print("\n🎉 Análise finalizada! Verifique a pasta '../dados' para os resultados.")
        return 0
    else:
        print("\n💥 Análise falhou. Verifique os erros acima.")
        return 1

if __name__ == "__main__":
    sys.exit(main())
