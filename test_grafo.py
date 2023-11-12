import unittest
from unittest.mock import patch
from io import StringIO
import sys
import time

from main import Grafo

class TestGrafoMethods(unittest.TestCase):

    def setUp(self):
        self.held_output = None
        self.num_vertices = 5
        self.grafo = Grafo(self.num_vertices)
        self.redirect_output()

    def redirect_output(self):
        self.held_output = StringIO()
        sys.stdout = self.held_output

    def release_output(self):
        output = self.held_output.getvalue().strip()
        self.held_output.close()
        sys.stdout = sys.__stdout__
        return output

    def test_cria_aresta(self):
        self.grafo.cria_aresta(1, 2)
        output = self.release_output()
        self.assertIn("Aresta entre 1 e 2 criada.", output)

    def test_remove_aresta(self):
        self.grafo.cria_aresta(1, 2)
        self.grafo.remove_aresta(1, 2)
        output = self.release_output()
        self.assertIn("Aresta entre 1 e 2 removida.", output)

    def test_pondera_rotula_vertice(self):
        self.grafo.pondera_rotula_vertice(1, 3.5, "A")
        output = self.release_output()
        self.assertIn("Vértice 1 ponderado com peso 3.5 e rotulado como 'A'.", output)

    def test_pondera_rotula_aresta(self):
        self.grafo.cria_aresta(1, 2)
        self.grafo.pondera_rotula_aresta(1, 2, 2.0, "B")
        output = self.release_output()
        self.assertIn("Aresta entre 1 e 2 ponderada com peso 2.0 e rotulada como 'B'.", output)

    def test_checa_existencia_aresta(self):
        self.grafo.cria_aresta(1, 2)
        self.assertTrue(self.grafo.checa_existencia_aresta(1, 2))

    def test_checa_grafo_vazio(self):
        self.assertTrue(self.grafo.checa_grafo_vazio())

    def test_checa_grafo_completo(self):
        self.grafo.cria_aresta(0, 1)
        self.grafo.cria_aresta(0, 2)
        self.grafo.cria_aresta(0, 3)
        self.grafo.cria_aresta(0, 4)
        self.assertTrue(self.grafo.checa_grafo_completo())

    def test_checa_quantidade_vertices_arestas(self):
        vertices, arestas = self.grafo.checa_quantidade_vertices_arestas()
        self.assertEqual(vertices, self.num_vertices)
        self.assertEqual(arestas, 0)

if __name__ == '__main__':
    unittest.main()
