import lista_encadeada as myList

class PilhaEncadeada(myList.LinkedList):
    """Estrutura de dados do tipo pilha (ordem LIFO) implementada com encadeamento
    
    Permite instanciar uma pilha encadeada, que herda a estrutura de nós da classe LinkedList.

    Atributos:
        qt (int): quantidade de elementos na pilha
    """
    def __init__(self):
        """Instancia um elemento da classe quando esta é chamada
        
        Complexity:
            Tempo: O(1)
            Espaço: O(1)"""
        super().__init__()
        self.qt = 0

    def push(self,data):
        """Insere um novo elemento na pilha

        Args:
            data (Any): valor a ser inserido
        Complexity:
            Tempo: O(1)
            Espaço: O(1)
        """
        no = myList.Node(data)
        no.next = self.head
        self.head = no
        self.qt += 1

    def pop(self):
        """Remove o último elemento inserido na pilha
        
        Returns:
            Any: o valor elemento removido
        Raises:
            IndexError: Se a pilha estiver vazia
        Complexity:
            Tempo: O(1)
            Espaço: O(1)
        """
        if self.esta_vazia():
            raise IndexError("A pilha está vazia")
        value = self.head.value
        self.head = self.head.next
        self.qt -= 1
        return value

    def topo(self):
        """Retorna o elemento no topo da pilha (último inserido)
        
        Returns:
            Any: O valor do topo da lista
        
        Raises:
            IndexError: Se a pilha estiver vazia
        Complexity:
            Tempo: O(1)
            Espaço: O(1)
        """
        if self.head == None:
            raise IndexError
        return self.head.value

    def esta_vazia(self):
        """Verifica se a pilha está vazia
        
        Returns:
            True (bool): Se estiver vazia
            False (bool): Se não estiver vazia
        Complexity:
            Tempo: O(1)
            Espaço: O(1)"""
        if self.qt == 0:
            return True
        else:
            return False

    def __len__(self):
        """Retorna a quantidade de elementos na pilha
        
        Returns:
            int: Quantidade de elementos
        Complexity:
            Tempo: O(1)
            Espaço: O(1)"""
        return self.qt

    def __repr__(self):
        """Define uma representação textual para as instâncias da classe
        
        Returns:
            string: String no formato "Pilha encadeada([elementos])".
        Raises:
            IndexError: Se a lista estiver vazia
        Complexity:
            Tempo: O(n), onde n é tamanho da pilha
            Espaço: O(n), onde n é o tamanho da string"""
        if self.esta_vazia():
            return f"PilhaEncadeada([])"
        text = "PilhaEncadeada(["
        for i in self:
            text += f"{i},"
        text = text[:-1]
        text += "])"

        return text
        
    def __iter__(self):
        """Itera sobre os elementos da pilha do topo até a base.
        
        Returns:
            Any: Valor do elemento atual da pilha seguindo a ordem LIFO
        Complexity:
            Tempo: O(n) para iteração da pilha completa, O(1) por passo
            Espaço: O(1)"""
        atual = self.head
        while atual is not None:
            yield atual.value
            atual = atual.next