# python 3

"""
maze_builder.py
---------------
Geração procedural de labirintos perfeitos usando busca em profundidade (DFS)
com retrocesso (backtracking).

Um labirinto "perfeito" possui exatamente um caminho entre quaisquer dois
pontos — equivalente a uma árvore geradora aleatória sobre a grade m x n.

Representação interna
~~~~~~~~~~~~~~~~~~~~~
A grade lógica de m linhas X n colunas é expandida para uma matriz de
(2m+1) X (2n+1) células, onde:
  - células de coordenadas ímpares (2i+1, 2j+1) representam salas (rooms);
  - células entre duas salas adjacentes representam paredes derrubáveis;
  - as bordas externas são sempre paredes.

O queijo (cheese) é colocado aleatoriamente em qualquer sala.
"""

import random


def generate_maze(m, n, room=0, wall=1, cheese='.'):
    """Gera um labirinto perfeito de m X n células usando DFS com backtracking.

    Parameters
    ----------
    m : int
        Número de linhas da grade lógica.
    n : int
        Número de colunas da grade lógica.
    room : int or str, optional
        Valor usado para representar passagens abertas. Padrão: 0.
    wall : int or str, optional
        Valor usado para representar paredes. Padrão: 1.
    cheese : str, optional
        Símbolo colocado aleatoriamente em uma sala como objetivo. Padrão: '.'.

    Returns
    -------
    list[list]
        Matriz (2m+1) X (2n+1) representando o labirinto gerado.
    """
    # Inicializa a matriz expandida com todas as células como parede
    maze = [[wall] * (2 * n + 1) for _ in range(2 * m + 1)]

    # Deslocamentos para os quatro vizinhos cardeais: N, S, W, E
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    def dfs(x, y):
        """Abre passagens recursivamente a partir da sala (x, y)."""
        maze[2 * x + 1][2 * y + 1] = room

        # Ordem aleatória garante labirintos distintos a cada execução
        random.shuffle(directions)

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                # Derruba a parede entre (x,y) e (nx,ny)
                maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                dfs(nx, ny)

    # Versão iterativa da função dfs
    def dfs_iter(x, y):
        pilha = [(x,y)]

        while pilha:
            # A versão recursiva implementa um pilha de chamadas implicitamente. Na versão iterativa, é preciso fazê-la explicitamente.
            x, y = pilha[-1]
            maze[2 * x + 1][2 * y + 1] = room

            # Embaralhar as direções
            random.shuffle(directions)

            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and maze[2 * nx + 1][2 * ny + 1] == wall:
                    # Derruba a parede entre (x,y) e (nx,ny)
                    maze[2 * x + 1 + dx][2 * y + 1 + dy] = room
                    pilha.append((nx,ny))
                    break
            else:
                pilha.pop()

    # Inicia a DFS no canto superior-esquerdo da grade lógica
    dfs_iter(0, 0)

    # Posiciona o queijo em uma sala aleatória (rejeita paredes)
    while True:
        i = int(random.uniform(0, 2 * m))
        j = int(random.uniform(0, 2 * m))
        if maze[i][j] == room:
            maze[i][j] = cheese
            break

    return maze

# Função que resolva o labirinto
def resolve_maze(maze, wall='W', cheese='*'):
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    pilha = [(0,0)]
    visitados = {(0,0)}
    m = (len(maze) - 1) // 2
    n = (len(maze[0]) - 1) // 2

    while pilha:
        x, y = pilha[-1]

        if maze[2 * x + 1][2 * y + 1] == cheese:
            return pilha
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n:
                passagem = maze[2 * x + 1 + dx][2 * y + 1 + dy]
                if passagem == cheese:
                    pilha.append((nx,ny))
                    return pilha
                aberto = passagem != wall
                nao_visitado = (nx,ny) not in visitados
                
                if aberto and nao_visitado:
                    visitados.add((nx,ny))
                    pilha.append((nx,ny))
                    break
        else:
            pilha.pop()
                
def print_maze(maze):
    """Imprime o labirinto no terminal, uma linha por vez.

    Parameters
    ----------
    maze : list[list]
        Matriz retornada por :func:`generate_maze`.
    """
    for row in maze:
        print(" ".join(map(str, row)))

def print_maze_solved(maze, caminho, path_icon="-", cheese="*"):
    maze_solved = [linhas.copy() for linhas in maze]

    for i in range(len(caminho) - 1):
        x1,y1 = caminho[i]
        x2,y2 = caminho[i + 1]

        l_sala, c_sala = 2 * x1 + 1, 2 * y1 + 1
        l_passagem, c_passagem = l_sala + (x2 - x1), c_sala + (y2 - y1)

        if maze_solved[l_sala][c_sala] != cheese:
            maze_solved[l_sala][c_sala] = path_icon
        if maze_solved[l_passagem][c_passagem] != cheese:
            maze_solved[l_passagem][c_passagem] = path_icon

    print_maze(maze_solved)

# Example usage:
if __name__ == '__main__':
    m, n = 25, 25  # Grid size
    random.seed(10110)
    room_icon = ' '
    wall_icon = 'W'
    cheese_icon = '*'
    maze = generate_maze(m, n, room=room_icon, wall=wall_icon, cheese=cheese_icon)
    print_maze_solved(maze, resolve_maze(maze), cheese=cheese_icon)