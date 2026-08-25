# 1
As classes bases devem ser **Pessoa, Iguaria e Restaurante**, porque remetem a conceitos mais gerais em relação às outras classes. 
Funcionário deve ser uma subclasse de pessoa (afinal, todo funcionário é uma pessoa) e deve ter garçom, chefe de cozinha e gerente como suas subclasses. A classe Funcionário herdaria os atributos de pessoa (*nome* e *idade*) e transmitiria para suas subclasses os atributos *salario* e *carga_horaria*.
Bolo e Pizza devem ser subclasses de iguaria, e neste caso herdariam *nome* e *preco* da sua classe mãe.
Pizzaria deve ser a única subclasse de restaurante, herdando dela seus atributos (*nome, endereco e telefone*)

# 2
A classe Restaurante poderia ter um novo atributo chamado *cardapio*, que seria uma lista de iguarias. Ao inicializar um restaurante, cada prato do cardápio seria instanciado, chamando a classe Iguaria, de modo que a pizza de um restaurante A não é a mesma pizza do restaurante B, apenas objetos da mesma classe.

# 3
- argumento1: Este argumento poderia ser uma string. Ao anotar um pedido, o garçom verificaria se há um prato no restaurante em que trabalha com esse nome. Se não houver, ele não completa o pedido, mas se sim, ele acrescenta a string em uma lista.
- argumento2: Este poderia ser uma string. Já foi verificado pelo garçom que o pedido do cliente é de fato um prato do cardápio, então o chefe receberia uma string com o nome do prato e instanciaria um objeto da classe Iguaria verificando o cardápio do restaurante em que trabalha.
- argumento3: Este deve ser uma instância da classe Funcionário. Antes de demitir o funcionário de fato, seria verificado se ele trabalha no mesmo restaurante do gerente ou não.