import sys
import time
import random
from collections import defaultdict

class GrafoDirecionado:
    def __init__(self):
        self.lista_adjacencia = defaultdict(set)
        self.pesos_arestas = {}
        self.vertices = 0

    def adiciona_vertice(self, vertice):
        self.lista_adjacencia[vertice]

    def cria_aresta(self, vertice_origem, vertice_destino, peso=1):
        self.adiciona_vertice(vertice_origem)
        self.adiciona_vertice(vertice_destino)
        self.lista_adjacencia[vertice_origem].add(vertice_destino)
        self.pesos_arestas[(vertice_origem, vertice_destino)] = peso

    def remove_aresta(self, vertice_origem, vertice_destino):
        self.lista_adjacencia[vertice_origem].remove(vertice_destino)
        del self.pesos_arestas[(vertice_origem, vertice_destino)]

    def busca_em_profundidade_iterativa(self, vertice, visitados, parent, tempo, low, descoberto):
        stack = [(vertice, iter(self.lista_adjacencia[vertice]))]

        while stack:
            vertice_atual, vizinhos = stack[-1]

            try:
                vizinho = next(vizinhos)
                vizinhos_vertice = iter(self.lista_adjacencia[vizinho])
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    parent[vizinho] = vertice_atual
                    tempo[0] += 1
                    descoberto[vizinho] = low[vizinho] = tempo[0]
                    stack.append((vizinho, vizinhos_vertice))
                elif vizinho != parent[vertice_atual]:
                    low[vertice_atual] = min(low[vertice_atual], descoberto[vizinho])
            except StopIteration:
                stack.pop()

        return low

    def identifica_pontes_naive(self):
        visitados = set()
        parent = defaultdict(lambda: -1)
        tempo = [0]
        low = defaultdict(lambda: float("inf"))
        descoberto = defaultdict(lambda: float("inf"))

        for vertice in range(self.vertices):
            if vertice not in visitados:
                self.busca_em_profundidade_iterativa(vertice, visitados, parent, tempo, low, descoberto)

        print("Pontes identificadas (naive)")

    def identifica_pontes_tarjan(self):
        visitados = set()
        tempo = [0]
        low = defaultdict(lambda: float("inf"))
        descoberto = defaultdict(lambda: float("inf"))

        def dfs(vertice, pai):
            nonlocal tempo
            tempo[0] += 1
            descoberto[vertice] = low[vertice] = tempo[0]
            for vizinho in self.lista_adjacencia[vertice]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    dfs(vizinho, vertice)
                    low[vertice] = min(low[vertice], low[vizinho])
                elif vizinho != pai:
                    low[vertice] = min(low[vertice], descoberto[vizinho])

        for vertice in range(self.vertices):
            if vertice not in visitados:
                visitados.add(vertice)
                dfs(vertice, -1)

        print("Pontes identificadas (Tarjan)")

    def gera_grafo_aleatorio(self, num_vertices):
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if random.choice([True, False]):
                    self.cria_aresta(i, j)
        return self

    def encontra_caminho_euleriano(self):
        if not self.checa_grafo_completo():
            print("O grafo não é euleriano.")
            return

        visitados = set()
        caminho = []

        def fleury(vertice):
            for vizinho in self.lista_adjacencia[vertice]:
                if (vertice, vizinho) not in self.pesos_arestas:
                    continue

                self.remove_aresta(vertice, vizinho)
                caminho.append((vertice, vizinho))
                fleury(vizinho)

        vertice_inicial = next(iter(self.lista_adjacencia.keys()))
        fleury(vertice_inicial)

        print("Caminho Euleriano:")
        for aresta in caminho:
            print(aresta)

    def checa_grafo_completo(self):
        return all(len(neighbors) % 2 == 0 for neighbors in self.lista_adjacencia.values())

    def teste_tempos_computacionais(self):
        for num_vertices in [100, 1000, 10000, 100000]:
            grafo = self.gera_grafo_aleatorio(num_vertices)

            self.vertices = num_vertices
            print(f"\nTestando para um grafo com {num_vertices} vértices:")

            start_time_naive = time.time()
            self.identifica_pontes_naive()
            end_time_naive = time.time()
            print(f"Tempo para identificar pontes (naive): {end_time_naive - start_time_naive} segundos")

            grafo = self.gera_grafo_aleatorio(num_vertices)

            start_time_tarjan = time.time()
            self.identifica_pontes_tarjan()
            end_time_tarjan = time.time()
            print(f"Tempo para identificar pontes (Tarjan): {end_time_tarjan - start_time_tarjan} segundos")

            grafo = self.gera_grafo_aleatorio(num_vertices)

            start_time_fleury = time.time()
            grafo.encontra_caminho_euleriano()
            end_time_fleury = time.time()
            print(f"Tempo para encontrar caminho euleriano: {end_time_fleury - start_time_fleury} segundos")

if __name__ == "__main__":
    sys.setrecursionlimit(10**6)
    grafo = GrafoDirecionado()
    grafo.teste_tempos_computacionais()
