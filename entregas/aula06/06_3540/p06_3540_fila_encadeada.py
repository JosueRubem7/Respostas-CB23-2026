import p06_3540_pilha_encadeada as pilha

class FilaEncadeada():
    """Estrutura de dados do tipo fila encadeada (ordem FIFO).
    
    Permite instanciar uma fila encadeada, uma coleção de dados na qual os primeiros elementos inseridos têm prioridade na ordem de saída

    Atributos:
        ent (PilhaEncadeada): pilha encadeada dos elementos que acabaram de entrar
        sai (PilhaEncadeada): pilha encadeada dos elementos que estão prestes a serem retirados (foram movidos da pilha de entrada para esta)
        qt (int): quantidade de elementos na fila encadeada
    """

    def __init__(self):
        """Instancia um objeto da classe quando esta é chamada.
        
        Complexity:
            Tempo: O(1)
            Espaço: O(1)"""
        self.ent = pilha.PilhaEncadeada()
        self.sai = pilha.PilhaEncadeada()

    def enfileirar(self, dado):
        """Adiciona um elemento novo na fila. Este elemento é inserido da pilha de entrada.
        
        Args:
            dado (any): Elemento a ser inserido
        Complexity:
            Tempo: O(1)
            Espaço: O(1)"""
        self.ent.push(dado)


    def desenfileirar(self):
        """Retira um elemento da fila, obedecendo a ordem de prioridade (FIFO).

        Returns: 
            Any: Elemento retirado da fila.
        Raises:
            IndexError: Se a pilha estiver vazia.
        Complexity:
            Tempo: O(n) no pior caso, onde n é o tamanho da lista de entrada | O(1) amortizado
            Espaço: O(1)"""
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        if len(self.sai) == 0:
            while len(self.ent) > 0:
                self.sai.push(self.ent.pop())
        return self.sai.pop()
        
    def frente(self):
        """Informa qual elemento será o próximo a sair. Não retira o elemento da fila.
        
        Returns:
            Any: Valor do elemento na frente da fila (maior prioridade de saída). 
        Raises:
            IndexError: Se a fila estiver vazia
        Complexity:
            Tempo: O(n) no pior caso, onde n é tamanho da lista de entrada | O(1) amortizado
            Espaço: O(1)"""
        
        if self.esta_vazia():
            raise IndexError("A fila está vazia")
        if len(self.sai) == 0:
            while len(self.ent) > 0:
                self.sai.push(self.ent.pop())
        return self.sai.topo()
    
    def esta_vazia(self):
        """Verifica se a fila está vazia.
        
        Returns:
            bool: Retorna True se a fila estiver vazia e False caso contrário.
        Complexity:
            Tempo: O(1)
            Espaço: O(1)"""
        return (len(self.ent) + len(self.sai)) == 0

    def __len__(self):
        """Retorna quantos elementos há na fila
        
        Returns:
            int: Quantidade de elementos na fila
        Complexity:
            Tempo: O(1)
            Espaço: O(1)"""
        return (len(self.ent) + len(self.sai))

    def __repr__(self):
        """Define uma representação textual para um objeto da classe
        
        Returns:
            string: String no formato "FilaEncadeada([elementos])".
        Complexity:
            Tempo: O(n), onde n é o tamanho das pilhas
            Espaço: O(n), onde n é o tamanho da pilha auxiliar e da string final"""
        if self.esta_vazia():
            return "FilaEncadeada([])"
        resultado = "FilaEncadeada(["
        tempo = pilha.PilhaEncadeada()
        
        for i in self.sai:
            resultado += f"{i},"

        while not self.ent.esta_vazia():
            tempo.push(self.ent.pop())
        while not tempo.esta_vazia():
            valor = tempo.pop()
            resultado += f"{valor},"
            self.ent.push(valor)
        resultado = resultado[:-1] + "])"
        
        return resultado