# Análise de complexidade da atividade 6
## Pilha encadeada
- push(): Tem complexidade sempre O(1), pois inserir um elemento novo na pilha não precisa mover nenhum outro, apenas adicioná-lo no topo.
- pop(): O(1), porque apenas retira o elemento que está no topo, sem mover nenhum outro.
- topo(): O(1), porque apenas verifica o elemento do topo e retorna o seu valor.
- esta_vazia(): O(1), porque apenas verifica se o atributo quantidade da pilha (contador) é maior do que zero.
- len(): O(1), porque apenas retorna o valor do contador.
- __repr__(): O(n), onde n é o tamanho da pilha. A função itera sobre os elementos da pilha,, adicionando-s um a um em uma string.
- __iter__(): 0(n) para uma iteração completa sobre a pilha, onde n é o tamanho dela, e O(1) para cada passo da iteração.

## Fila encadeada
- enfileirar(): O(1), pois apenas adiciona um elemento novo na pilha de entrada.
- desenfileirar(): No pior caso, que é quando não há elementos na lista de saída, leva tempo O(n), onde n é o tamanho da lista de entrada. Mas se a pilha de saída não estiver vazia, basta retirar o elemento do topo desta, pelo que a complexidade é O(1) amortizada neste caso.
- frente(): Se a pilha de saída estiver vazia (pior caso), é preciso "virar" toda a pilha de entrada na pilha de saída e depois retornar o topo, logo a complexidade é O(n), porém quando há elementos na pilha de saída, a complexidade é O(1) amortizada.
- esta_vazia(): O(1), porque apenas verifica o tamanho das duas pilhas, soma-os, verifica se o resultado é nulo e retorna o booleano da comparação.
- len(): O(1), apenas soma os tamanhos das pilhas e apresenta o resultado.
- repr(): 0(n) de tempo, onde n é o tamanho das pilhas. Todos os valores da pilha de saída são colocados na string inicialmente, o que é 0(n). Depois a pilha de entrada (caso tenha elementos) é virada em uma pilha temporária, já que na ordem original os elementos estariam ao contrário. Por fim, colocamos cada elemento da lista temporária na string enquanto retornamos eles para a pilha de entrada, o que é O(n).