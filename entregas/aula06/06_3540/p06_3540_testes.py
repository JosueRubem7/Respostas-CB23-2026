import unittest
import importlib

pilha_enc = importlib.import_module("p06_3540_pilha_encadeada")
fila_enc = importlib.import_module("p06_3540_fila_encadeada")

class TestPilhaEncadeada(unittest.TestCase):

    def setUp(self):
        """Inicializa uma instância limpa da pilha antes de cada teste."""
        self.pilha = pilha_enc.PilhaEncadeada()

    def test_ordem_lifo(self):
        """Testa a ordem LIFO em uma sequência contínua de push e pop."""
        elementos = ["primeiro", "segundo", "terceiro"]
        for elem in elementos:
            self.pilha.push(elem)

        self.assertEqual(self.pilha.pop(), "terceiro")
        self.assertEqual(self.pilha.pop(), "segundo")
        self.assertEqual(self.pilha.pop(), "primeiro")

    def test_pop_e_topo_em_pilha_vazia(self):
        """Testa se pop() e topo() lançam IndexError quando a pilha está vazia."""
        with self.assertRaises(IndexError):
            self.pilha.pop()

        with self.assertRaises(IndexError):
            self.pilha.topo()

    def test_coerencia_len(self):
        """Testa a precisão do tamanho (len) durante inserções e remoções."""
        self.assertEqual(len(self.pilha), 0)

        self.pilha.push(10)
        self.pilha.push(20)
        self.assertEqual(len(self.pilha), 2)

        self.pilha.pop()
        self.assertEqual(len(self.pilha), 1)

        self.pilha.pop()
        self.assertEqual(len(self.pilha), 0)

    def test_alternancia_operacoes(self):
        """Testa a alternância contínua entre push, topo e pop."""
        self.pilha.push("A")
        self.pilha.push("B")
        self.assertEqual(self.pilha.pop(), "B")

        self.pilha.push("C")
        self.assertEqual(self.pilha.topo(), "C")
        self.assertEqual(self.pilha.pop(), "C")
        self.assertEqual(self.pilha.pop(), "A")

    def test_tipos_diferentes_repetidos_e_none(self):
        """Testa o armazenamento de múltiplos tipos, valores duplicados e None."""
        dados = [100, "Python", None, 100, [1, 2], None]

        for item in dados:
            self.pilha.push(item)

        for item in reversed(dados):
            self.assertEqual(self.pilha.pop(), item)


class TestFilaEncadeada(unittest.TestCase):

    def setUp(self):
        """Inicializa uma instância limpa da fila antes de cada teste."""
        self.fila = fila_enc.FilaEncadeada()

    def test_ordem_fifo(self):
        """Testa a ordem FIFO (primeiro a entrar é o primeiro a sair)."""
        self.fila.enfileirar(1)
        self.fila.enfileirar(2)
        self.fila.enfileirar(3)

        self.assertEqual(self.fila.desenfileirar(), 1)
        self.assertEqual(self.fila.desenfileirar(), 2)
        self.assertEqual(self.fila.desenfileirar(), 3)

    def test_intercalacao_enfileirar_desenfileirar(self):
        """Testa chamadas intercaladas de enfileirar, frente e desenfileirar."""
        self.fila.enfileirar("A")
        self.fila.enfileirar("B")
        self.assertEqual(self.fila.desenfileirar(), "A")

        self.fila.enfileirar("C")
        self.assertEqual(self.fila.frente(), "B")
        self.assertEqual(self.fila.desenfileirar(), "B")
        self.assertEqual(self.fila.desenfileirar(), "C")

    def test_esvaziar_e_voltar_a_usar_mesma_instancia(self):
        """Testa o esvaziamento completo e reuso da mesma instância."""
        # Primeiro ciclo de uso
        self.fila.enfileirar(10)
        self.fila.enfileirar(20)
        self.assertEqual(self.fila.desenfileirar(), 10)
        self.assertEqual(self.fila.desenfileirar(), 20)
        self.assertTrue(self.fila.esta_vazia())

        # Segundo ciclo de uso na mesma instância
        self.fila.enfileirar(30)
        self.fila.enfileirar(40)
        self.assertEqual(self.fila.frente(), 30)
        self.assertEqual(self.fila.desenfileirar(), 30)
        self.assertEqual(self.fila.desenfileirar(), 40)
        self.assertTrue(self.fila.esta_vazia())

    def test_desenfileirar_e_frente_em_fila_vazia(self):
        """Testa se desenfileirar() e frente() lançam IndexError em fila vazia."""
        with self.assertRaises(IndexError):
            self.fila.desenfileirar()

        with self.assertRaises(IndexError):
            self.fila.frente()

    def test_coerencia_len(self):
        """Testa se len reflete exatamente a quantidade de elementos na fila."""
        self.assertEqual(len(self.fila), 0)

        self.fila.enfileirar("X")
        self.fila.enfileirar("Y")
        self.assertEqual(len(self.fila), 2)

        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 1)

        self.fila.desenfileirar()
        self.assertEqual(len(self.fila), 0)

    def test_repr_nao_corrompe_fila(self):
        """Testa se chamar repr() não altera o estado interno da fila."""
        self.fila.enfileirar(10)
        self.fila.enfileirar(20)
        
        # Chama a representação textual
        texto = repr(self.fila)
        self.assertEqual(texto, "FilaEncadeada([10,20])")
        
        # Verifica se os elementos continuam intactos após o repr
        self.assertEqual(len(self.fila), 2)
        self.assertEqual(self.fila.desenfileirar(), 10)
        self.assertEqual(self.fila.desenfileirar(), 20)
if __name__ == "__main__":
    unittest.main()