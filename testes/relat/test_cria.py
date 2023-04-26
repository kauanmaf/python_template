import unittest
from relatorio.cria import Relatório

class TestCria(unittest.TestCase):
    def test_cria_realtorio(self):
        R = Relatório('Meu Relatório', 'Eu mesmo')
        self.assertEqual(R.titulo, 'Meu relatório')