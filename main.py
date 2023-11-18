import time

class Grafo:
    def __init__(self, vertices):
        self.vertices = vertices
        self.matriz_adjacencia = [[0] * vertices for _ in range(vertices)]
        self.lista_adjacencia = {i: set() for i in range(vertices)}
        self.pesos_arestas = {}
        self.rotulos_arestas = {}
        self.pesos_vertices = {}
        self.rotulos_vertices = {}

    def cria_aresta(self, v1, v2):
        if 0 <= v1 < self.vertices and 0 <= v2 < self.vertices:
            self.matriz_adjacencia[v1][v2] = 1
            self.matriz_adjacencia[v2][v1] = 1
            self.lista_adjacencia[v1].add(v2)
            self.lista_adjacencia[v2].add(v1)
            print(f"Aresta entre {v1} e {v2} criada.")
        else:
            print("Vértice fora da faixa válida.")
        self.exibe_grafo()

    def remove_aresta(self, v1, v2):
        if 0 <= v1 < self.vertices and 0 <= v2 < self.vertices:
            if self.matriz_adjacencia[v1][v2] == 1:
                self.matriz_adjacencia[v1][v2] = 0
                self.matriz_adjacencia[v2][v1] = 0
                self.lista_adjacencia[v1].remove(v2)
                self.lista_adjacencia[v2].remove(v1)
                print(f"Aresta entre {v1} e {v2} removida.")
                self.pesos_arestas.pop((v1, v2), None)
                self.rotulos_arestas.pop((v1, v2), None)
            else:
                print(f"Aresta entre {v1} e {v2} não existe.")
        else:
            print("Vértice fora da faixa válida.")
        self.exibe_grafo()

    def pondera_rotula_vertice(self, vertice, peso, rotulo):
        if 0 <= vertice < self.vertices:
            self.pesos_vertices[vertice] = peso
            self.rotulos_vertices[vertice] = rotulo
            print(f"Vértice {vertice} ponderado com peso {peso} e rotulado como '{rotulo}'.")
            return vertice
        else:
            print("Vértice fora da faixa válida.")
            return False


    def pondera_rotula_aresta(self, v1, v2, peso, rotulo):
        if 0 <= v1 < self.vertices and 0 <= v2 < self.vertices:
            if self.matriz_adjacencia[v1][v2] == 1:
                self.pesos_arestas[(v1, v2)] = peso
                self.rotulos_arestas[(v1, v2)] = rotulo
                print(f"Aresta entre {v1} e {v2} ponderada com peso {peso} e rotulada como '{rotulo}'.")
            else:
                print("Aresta não existe.")
        else:
            print("Vértice fora da faixa válida.")
        self.exibe_grafo()

    def checa_adjacencia_vertice(self, v1, v2):
        if 0 <= v1 < self.vertices and 0 <= v2 < self.vertices:
            resultado = self.matriz_adjacencia[v1][v2] == 1
            print(f"Vértice {v1} é adjacente a {v2}.") if resultado else print(f"Vértice {v1} não é adjacente a {v2}.")
            return resultado
        else:
            print("Vértice fora da faixa válida.")
            return False

    def pondera_rotula_aresta(self, v1, v2, peso, rotulo):
        if 0 <= v1 < self.vertices and 0 <= v2 < self.vertices:
            if self.matriz_adjacencia[v1][v2] == 1:
                self.pesos_arestas[(v1, v2)] = peso
                self.rotulos_arestas[(v1, v2)] = rotulo
                print(f"Aresta entre {v1} e {v2} ponderada com peso {peso} e rotulada como '{rotulo}'.")
            else:
                print("Aresta não existe.")
        else:
            print("Vértice fora da faixa válida.")
        self.exibe_grafo()

    def checa_existencia_aresta(self, v1, v2):
        if 0 <= v1 < self.vertices and 0 <= v2 < self.vertices:
            resultado = self.matriz_adjacencia[v1][v2] == 1
            print(f"Aresta entre {v1} e {v2} existe.") if resultado else print(f"Aresta entre {v1} e {v2} não existe.")
            return resultado
        else:
            print("Vértice fora da faixa válida.")
            return False

    def checa_adjacencia_aresta(self, v1, v2):
        if 0 <= v1 < self.vertices and 0 <= v2 < self.vertices:
            resultado = self.matriz_adjacencia[v1][v2] == 1
            print(f"Aresta entre {v1} e {v2} é adjacente.") if resultado else print(f"Aresta entre {v1} e {v2} não é adjacente.")
            return resultado
        else:
            print("Vértice fora da faixa válida.")
            return False

    def checa_quantidade_vertices_arestas(self):
        num_arestas = sum(sum(row) for row in self.matriz_adjacencia) // 2
        vertices, arestas = self.vertices, num_arestas
        print(f"O grafo tem {vertices} vértices e {arestas} arestas.")
        return vertices, arestas

    def checa_grafo_vazio(self):
        resultado = all(all(cell == 0 for cell in row) for row in self.matriz_adjacencia)
        print("O grafo está vazio.") if resultado else print("O grafo não está vazio.")
        return resultado

    def checa_grafo_completo(self):
        completo = all(sum(row) == self.vertices - 1 for row in self.matriz_adjacencia)
        reflexivo = all(self.matriz_adjacencia[i][i] == 0 for i in range(self.vertices))
        resultado = completo and reflexivo
        print("O grafo é completo.") if resultado else print("O grafo não é completo.")
        return resultado

    def exibe_grafo(self):
        print("\nMatriz de Adjacência:")
        for row in self.matriz_adjacencia:
            print(row)

        print("\nLista de Adjacência:")
        for vertice, vizinhos in self.lista_adjacencia.items():
            print(f"{vertice}: {list(vizinhos)}")

        print("\nPesos das Arestas:")
        for aresta, peso in self.pesos_arestas.items():
            v1, v2 = aresta
            print(f"Aresta entre {v1} e {v2}: Peso {peso}")

        print("\nRótulos das Arestas:")
        for aresta, rotulo in self.rotulos_arestas.items():
            v1, v2 = aresta
            print(f"Aresta entre {v1} e {v2}: Rótulo {rotulo}")

        print("\nPesos dos Vértices:")
        for vertice, peso in self.pesos_vertices.items():
            print(f"Vértice {vertice}: Peso {peso}")

        print("\nRótulos dos Vértices:")
        for vertice, rotulo in self.rotulos_vertices.items():
            print(f"Vértice {vertice}: Rótulo {rotulo}")


def menu():
    print("\nEscolha uma opção:")
    print("1. Criar aresta")
    print("2. Remover aresta")
    print("3. Ponderar e rotular vértice")
    print("4. Ponderar e rotular aresta")
    print("5. Checar adjacência entre vértices")
    print("6. Checar existência de aresta")
    print("7. Checar adjacência entre arestas")
    print("8. Checar quantidade de vértices e arestas")
    print("9. Checar se o grafo está vazio")
    print("10. Checar se o grafo é completo")
    print("11. Exibir grafo")
    print("0. Sair")


if __name__ == "__main__":
    num_vertices = int(input("Digite o número de vértices: "))
    grafo = Grafo(num_vertices)

    while True:
        menu()

        try:
            escolha = int(input("Digite o número da opção desejada: "))
        except ValueError:
            print("Por favor, insira um número inteiro válido.")
            continue

        if escolha == 1:
            try:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
            except ValueError:
                print("Por favor, insira números inteiros válidos.")
                continue
            grafo.cria_aresta(v1, v2)
        elif escolha == 2:
            try:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
            except ValueError:
                print("Por favor, insira números inteiros válidos.")
                continue
            grafo.remove_aresta(v1, v2)
        elif escolha == 3:
            try:
                vertice = int(input("Digite o vértice a ser ponderado: "))
                peso = float(input("Digite o peso do vértice: "))
                rotulo = input("Digite o rótulo do vértice: ")
            except ValueError:
                print("Por favor, insira números e texto válidos.")
                continue
            grafo.pondera_rotula_vertice(vertice, peso, rotulo)
        elif escolha == 4:
            try:
                v1 = int(input("Digite o primeiro vértice da aresta: "))
                v2 = int(input("Digite o segundo vértice da aresta: "))
                peso = float(input("Digite o peso da aresta: "))
                rotulo = input("Digite o rótulo da aresta: ")
            except ValueError:
                print("Por favor, insira números e texto válidos.")
                continue
            grafo.pondera_rotula_aresta(v1, v2, peso, rotulo)
        elif escolha == 5:
            try:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
            except ValueError:
                print("Por favor, insira números inteiros válidos.")
                continue
            grafo.checa_adjacencia_vertice(v1, v2)
        elif escolha == 6:
            try:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
            except ValueError:
                print("Por favor, insira números inteiros válidos.")
                continue
            grafo.checa_existencia_aresta(v1, v2)
        elif escolha == 7:
            try:
                v1 = int(input("Digite o primeiro vértice: "))
                v2 = int(input("Digite o segundo vértice: "))
            except ValueError:
                print("Por favor, insira números inteiros válidos.")
                continue
            grafo.checa_adjacencia_aresta(v1, v2)
        elif escolha == 8:
            grafo.checa_quantidade_vertices_arestas()
        elif escolha == 9:
            grafo.checa_grafo_vazio()
        elif escolha == 10:
            grafo.checa_grafo_completo()
        elif escolha == 11:
            grafo.exibe_grafo()

        time.sleep(3)
        if escolha == 0:
            break
