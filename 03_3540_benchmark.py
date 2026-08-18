import AulasPraticas.AP_03_ordenacao as ap3
import time
import sys
import random

sys.setrecursionlimit(10**6)

def caso_medio(n):
    original = []
    for i in range(1,n + 1):
        original.append(i)
    lista = []
    while len(original):
        rand_index = random.randint(0, len(original) - 1)
        lista.append(original[rand_index])
        original[rand_index],original[-1] = original[-1],original[rand_index]
        original.pop(-1)
    return lista

def list_invertida(n):
    return list(range(n,0,-1))

def perf_algo(sort_algo:function,N,k,worst_case_fun= None):
    times = []
    for _ in range(k):
        test_list = worst_case_fun(N) if worst_case_fun else caso_medio(N)
        start_t = time.perf_counter()
        sort_algo(test_list)
        end_t = time.perf_counter()
        times.append(end_t - start_t)
    return sum(times)/k

valores_N = [20, 100, 500, 1000]
k = 50

algoritmos = [
    ("Quick Sort", ap3.quick_sort),
    ("Selection Sort", ap3.selection_sort),
    ("Merge Sort", ap3.divide_and_conquer_sort)
]

dados_testes = []

for nome_algo, func_algo in algoritmos:
    for N in valores_N:
        medio = perf_algo(func_algo, N, k)
        pior = perf_algo(func_algo, N, k, list_invertida)
        dados_testes.append([nome_algo, N, medio, pior])

print(f"\nQuantidade de testes por algoritmo/cenário: {k}\n")

print(f"{'Algoritmo':<18} | {'Tamanho (N)':<12} | {'Caso Médio (s)':<25} | {'Pior Caso (s)':<25}")
print("-" * 87)

algo_atual = dados_testes[0][0]

for algoritmo, n_val, medio, pior in dados_testes:
    if algoritmo != algo_atual:
        print("-" * 87)
        algo_atual = algoritmo
        
    print(f"{algoritmo:<18} | {n_val:<12} | {medio:<25} | {pior:<25}")

print("\n")