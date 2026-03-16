# Gerenciador de Estoque em Python

Sistema de gerenciamento de inventário desenvolvido em Python para controle de produtos, preços e movimentação de vendas, utilizando uma interface visual no terminal.

---

## Funcionalidades

### Cadastro de Itens
Registro detalhado de produtos com geração automática de identificadores (ID) baseados no nome.

### Tabela de Inventário
Visualização organizada utilizando a biblioteca Rich, com destaque visual para níveis de estoque:

- Crítico
- Baixo
- Disponível



### Módulo de Vendas
Sistema de vendas com:

- Validação de quantidade disponível
- Cálculo automático de subtotal
- Confirmação de transação

### Cálculo de Patrimônio
Ferramenta que calcula o valor total de todos os itens em estoque, permitindo uma análise financeira rápida.

### Arquitetura de Menu
Sistema de navegação estruturado para:

- Melhor organização
- Uso eficiente de memória
- Evitar erros de recursão



---

## Tecnologias Utilizadas

- Python 3.x

Bibliotecas utilizadas:

- **rich**: Interface visual no terminal
- **os**: Comandos do sistema
- **random**: Geração de dados

---

## Como Executar

### 1. Certifique-se de ter o Python instalado

Verifique com:
 ```Bash
python --version
 ```
### 2. Instale a biblioteca necessária
Utilize o gerenciador de pacotes pip:
 ```Bash
pip install rich
 ```
### 3. Execute o programa
No terminal, dentro da pasta do projeto, digite:

 ```Bash
python main.py
 ```
## Estrutura do Projeto
O código está dividido em módulos para facilitar a leitura e manutenções futuras:

 - main.py: Ponto de entrada e inicialização do sistema.

- Modelos/produto.py: Definição da classe Produto e seus atributos fundamentais.

- Modelos/funcao.py: Lógica central, validações de estoque e interface de usuário.

### Créditos e Autoria
Este projeto foi desenvolvido através de um processo colaborativo:

### Conceito e Orientação Técnica:
A estrutura lógica, estratégias de depuração e a arquitetura de loops foram orientadas pelo Gemini (IA da Google).

### Desenvolvimento e Implementação:
Toda a execução do código, lógica de vendas, organização de classes e testes práticos foram realizados integralmente por Luca.

Contato: Luca - lucagopro12@gmail.com

### Documentação:
O texto deste README foi redigido pelo Gemini sob supervisão do desenvolvedor.

**Aviso**: Este código é público e pode ser utilizado ou compartilhado por qualquer pessoa, desde que seja citada a base original e a autoria de Luca. O projeto representa um estágio de aprendizado e desenvolvimento, portanto, o código pode sofrer alterações estruturais, refatorações ou adição de novas funcionalidades no futuro conforme o autor evoluir em seus estudos.
