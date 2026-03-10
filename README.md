Gerenciador de Estoque Python
Sistema de gerenciamento de inventário desenvolvido em Python para controle de produtos, preços e movimentação de vendas, utilizando uma interface visual via terminal.

Funcionalidades
Cadastro de Itens: Registro detalhado de produtos com geração de identificadores (ID) baseados no nome.

Tabela de Inventário: Exibição organizada utilizando a biblioteca Rich, com destaque visual para níveis de estoque (Crítico, Baixo e Disponível).

Módulo de Vendas: Sistema com validação de quantidade disponível, cálculo de subtotal e confirmação de transação.

Cálculo de Patrimônio: Ferramenta de análise financeira que soma o valor total de todos os itens em estoque.

Arquitetura de Menu: Navegação baseada em um laço de repetição infinito (while True), otimizando o uso de memória e evitando erros de recursão.

Tecnologias Utilizadas
Linguagem: Python 3.x

Bibliotecas: Rich (Interface), OS (Comandos de sistema), Random (Geração de dados).

Como Executar
Certifique-se de ter o Python instalado.

Instale a dependência necessária:
pip install rich

Execute o arquivo principal:
python main.py

Estrutura do Projeto
O código está dividido em módulos para facilitar a leitura e futuras manutenções:

main.py: Inicialização do sistema.

Modelos/produto.py: Definição da classe Produto e seus atributos.

Modelos/funcao.py: Lógica central, validações e interface de usuário.

Créditos e Autoria
Este projeto foi desenvolvido através de um processo colaborativo:

Conceito e Orientação Técnica: A estrutura lógica e estratégias de depuração foram orientadas pelo Gemini (IA da Google).

Desenvolvimento e Implementação: Toda a execução do código, lógica de vendas, organização de classes e testes práticos foram realizados integralmente por Luca.

Contato: Luca - lucagopro12@gmail.com

Documentação: O texto deste README foi redigido pelo Gemini sob supervisão do desenvolvedor.

Aviso: Este código é público e pode ser utilizado ou compartilhado por qualquer pessoa, desde que seja citada a base original e a autoria de Luca. O projeto representa um estágio de aprendizado e desenvolvimento, portanto, o código pode sofrer alterações estruturais, refatorações ou adição de novas funcionalidades no futuro conforme o autor evoluir em seus estudos.