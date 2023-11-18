import sys
import timeit
import random
from collections import defaultdict, deque

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
        self.pesos_arestas[frozenset((vertice_origem, vertice_destino))] = peso

    def remove_aresta(self, vertice_origem, vertice_destino):
        self.lista_adjacencia[vertice_origem].remove(vertice_destino)
        del self.pesos_arestas[frozenset((vertice_origem, vertice_destino))]

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

    def busca_em_profundidade_iterativa_otimizada(self, vertice, visitados, parent, tempo, low, descoberto):
        stack = [(vertice, iter(self.lista_adjacencia[vertice]))]

        while stack:
            vertice_atual, vizinhos = stack[-1]

            if vertice_atual not in visitados:
                visitados.add(vertice_atual)
                parent[vertice_atual] = None  # Inicializando o pai do primeiro vértice
                tempo[0] += 1
                descoberto[vertice_atual] = low[vertice_atual] = tempo[0]

            vizinho = next(vizinhos, None)
            while vizinho is not None:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    parent[vizinho] = vertice_atual
                    tempo[0] += 1
                    descoberto[vizinho] = low[vizinho] = tempo[0]
                    stack.append((vizinho, iter(self.lista_adjacencia[vizinho])))
                    break
                elif vizinho != parent[vertice_atual]:
                    low[vertice_atual] = min(low[vertice_atual], descoberto[vizinho])
                vizinho = next(vizinhos, None)

            if vizinho is None:
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

    def gera_grafo_aleatorio(self, num_vertices, probabilidade=0.1):
        for i in range(num_vertices):
            for j in range(i + 1, num_vertices):
                if random.random() < probabilidade:
                    aresta = frozenset((i, j))
                    if aresta not in self.pesos_arestas:
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
                aresta = frozenset((vertice, vizinho))
                if aresta in self.pesos_arestas:
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
            self.vertices = num_vertices
            print(f"\nTestando para um grafo com {num_vertices} vértices:")
            grafo = self.gera_grafo_aleatorio(num_vertices)

            time_naive = timeit.timeit(lambda: self.identifica_pontes_naive(), number=1)
            print(f"Tempo para identificar pontes (naive): {time_naive} segundos")

            grafo = self.gera_grafo_aleatorio(num_vertices)

            time_tarjan = timeit.timeit(lambda: self.identifica_pontes_tarjan(), number=1)
            print(f"Tempo para identificar pontes (Tarjan): {time_tarjan} segundos")

            grafo = self.gera_grafo_aleatorio(num_vertices)

            time_fleury = timeit.timeit(lambda: grafo.encontra_caminho_euleriano(), number=1)
            print(f"Tempo para encontrar caminho euleriano: {time_fleury} segundos")

if __name__ == "__main__":
    sys.setrecursionlimit(10**7)
    grafo = GrafoDirecionado()
    grafo.teste_tempos_computacionais()
