import random
import time
import tracemalloc
import matplotlib.pyplot as plt
import sys
import csv

sys.setrecursionlimit(10**7)

def heapsort(arr):
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
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

    return arr


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    for i in range(1, len(arr)):
        chave = arr[i]
        j = i - 1
        while j >= 0 and chave < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = chave
    return arr

def analisar_algoritmo(algoritmo, arr):
    arr_copy = arr.copy()
    tracemalloc.start()
    inicio = time.time()
    algoritmo(arr_copy)
    fim = time.time()
    memoria_atual, memoria_pico = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return fim - inicio, memoria_pico / 1024

def gerar_entradas(tamanho):
    return {
        "ordenada": list(range(tamanho)),
        "reversa": list(range(tamanho, 0, -1)),
        "aleatoria": random.sample(range(tamanho * 10), tamanho)
    }

def main():
    tamanhos = [10, 100, 1000, 10000]
    algoritmos = {
        "HeapSort": heapsort,
        "BubbleSort": bubble_sort,
        "SelectionSort": selection_sort,
        "InsertionSort": insertion_sort
    }

    resultados = []

    for n in tamanhos:
        entradas = gerar_entradas(n)
        for tipo, entrada in entradas.items():
            for nome, alg in algoritmos.items():
                tempo, memoria = analisar_algoritmo(alg, entrada)
                resultados.append((nome, tipo, n, tempo, memoria))
                print(f"{nome} | Entrada: {tipo} | n={n} -> Tempo: {tempo:.5f}s, Memória: {memoria:.2f}KB")
                
    with open("resultados_heapsort.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile, delimiter=";")
        writer.writerow(["Algoritmo", "TipoEntrada", "Tamanho", "TempoSegundos", "MemoriaKB"])
        for r in resultados:
            writer.writerow(r)

    print("\n✅ Resultados salvos em 'resultados_heapsort.csv'")

    for tipo in ["ordenada", "reversa", "aleatoria"]:
        plt.figure()
        for nome in algoritmos.keys():
            xs = [r[2] for r in resultados if r[0] == nome and r[1] == tipo]
            ys = [r[3] for r in resultados if r[0] == nome and r[1] == tipo]
            plt.plot(xs, ys, marker="o", label=nome)
        plt.title(f"Comparação de Tempo - Entrada {tipo}")
        plt.xlabel("Tamanho da entrada (n)")
        plt.ylabel("Tempo (s)")
        plt.legend()
        plt.grid()
        plt.show()

    for tipo in ["ordenada", "reversa", "aleatoria"]:
        plt.figure()
        for nome in algoritmos.keys():
            xs = [r[2] for r in resultados if r[0] == nome and r[1] == tipo]
            ys = [r[4] for r in resultados if r[0] == nome and r[1] == tipo]
            plt.plot(xs, ys, marker="o", label=nome)
        plt.title(f"Comparação de Memória - Entrada {tipo}")
        plt.xlabel("Tamanho da entrada (n)")
        plt.ylabel("Memória (KB)")
        plt.legend()
        plt.grid()
        plt.show()

if __name__ == "__main__":
    main()
