from Modelos.produto import Produto
from rich import print
from rich.traceback import install
from rich.progress import track
from rich.table import Table
from rich.panel import Panel
from random import randint
from os import system
install()

def volta_para_o_menu():
    input('Aperte enter para voltar pro menu: ')

def erro():
    print('[red]Algo deu errado[/]')
    volta_para_o_menu()
    
def vendas():
    titulo('Vender Produtos')
    if not lista_de_produto:
        print("Você não tem nenhum produto cadastrado.")
        input('aperte enter para ir cadastrar um produto: ')
        cadastrar_produto()
        return
    for indice, produtos in enumerate(lista_de_produto, start=1):
        print(indice, produtos.nome)
    print("\n(Digite 0 para voltar ao menu principal)")
    escolha = int(input('\nEscolha qual produto você vai vender: '))
    if escolha == 0:
        volta_para_o_menu()
        return
    produto_selecionado = lista_de_produto[escolha - 1]
    print(f"Você selecionou: {produto_selecionado.nome}")
    vendidos = int(input('Quantos produtos você vendeu? '))
    if vendidos > produto_selecionado.qnt:
        print('[red] Você esta tentando vendar mais produto que você tem.[/] Tente novamente.')
        input('Aperte Enter ')
        vendas()
    else:
        valor = vendidos * produto_selecionado.preco
        resposta_s_n(f'O Valor da compra é de {valor} quer proseguir? (s/n) ')
        produto_selecionado.qnt -= vendidos
        print(f'Falta {produto_selecionado.qnt}')
        print('[green]Produtos vendidos com sucesso![/]')
        volta_para_o_menu()

def menu():
    while True:
        system('cls')
        try:
            print(r""" ________              __                                             
        /        |            /  |                                            
        $$$$$$$$/   _______  _$$ |_     ______    ______   __    __   ______  
        $$ |__     /       |/ $$   |   /      \  /      \ /  |  /  | /      \ 
        $$    |   /$$$$$$$/ $$$$$$/   /$$$$$$  |/$$$$$$  |$$ |  $$ |/$$$$$$  |
        $$$$$/    $$      \   $$ | __ $$ |  $$ |$$ |  $$ |$$ |  $$ |$$    $$ |
        $$ |_____  $$$$$$  |  $$ |/  |$$ \__$$ |$$ \__$$ |$$ \__$$ |$$$$$$$$/ 
        $$       |/     $$/   $$  $$/ $$    $$/ $$    $$ |$$    $$/ $$       |
        $$$$$$$$/ $$$$$$$/     $$$$/   $$$$$$/   $$$$$$$ | $$$$$$/   $$$$$$$/ 
                                                    $$ |                    
                                                    $$ |                    
                                                    $$/                     
        """)
            numero_pergunta = int(input('Digite 0 para fechar o programa \n 1 para Cadastrar um Produto\n 2 para ver os produtos cadastrados\n 3 para vender um produto\n 4 para calcular patrimonio: '))

            if numero_pergunta == 1:
                cadastrar_produto()
            elif numero_pergunta == 0:
                    titulo('Fechar Programa')
                    resposta_s_n(texto='Você quer fechar o programa? (s/n) ')
                    break
            elif numero_pergunta == 2:
                ver_produto_cadastrado()
            elif numero_pergunta == 3:
                vendas()
            elif numero_pergunta == 4:
                calcular_patrimonio(lista_de_produto)
            else:
                erro()
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            erro()

def titulo(texto):
    system('cls')
    caixa = Panel(f'[red]{texto}[/]')
    print(caixa)

def gerador_de_id(nome):
    numero_aleatorio = randint(100, 999)
    letras = nome[:2].upper() 
    return f'{letras}{numero_aleatorio}'

lista_de_produto = []

def cadastrar_produto():
    titulo('Cadrastar Produto')
    nome_do_produto = input('Qual o nome do produto? ')
    preco = float(input('Qual o preço do produto? '))
    quantidade = int(input('Qual a quantidade que você tem do produto? '))
    codigo_id = gerador_de_id(nome=nome_do_produto)
    produto = Produto(nome_do_produto, preco, codigo_id ,quantidade)
    lista_de_produto.append(produto)
    print('[green]Produto cadastrado com sucesso[/]')
    volta_para_o_menu()
    
def ver_produto_cadastrado():
    titulo('Ver Produstos Cadastrados')
    
    if not lista_de_produto:
        print('[red]Você nāo tem nenhum produto cadastrado[/]\nVolte ao menu para cadastrar.')
        volta_para_o_menu()
        return 

    tabela = Table()
    tabela.add_column('Nome')
    tabela.add_column('Quantidade')
    tabela.add_column('ID')
    tabela.add_column('Preço')

    for i in lista_de_produto:
        if i.qnt == 0:
            estilo_linha = 'black on red'
        elif i.qnt <= 10:
            estilo_linha = 'black on yellow'
        else:
            estilo_linha = 'black on green'
        
        tabela.add_row(i.nome, str(i.qnt), str(i.id), str(i.preco), style=estilo_linha)


    print(tabela)
    volta_para_o_menu()    

def calcular_patrimonio(lista_de_produtos_outro):
    titulo('Calcular Patrimonio')
    total = 0
    for i in lista_de_produtos_outro:
        subtotal = i.qnt * i.preco
        total += subtotal
    
    painel = Panel(
        f"Valor Total em Estoque: R$ {total:,.2f}", 
        title="Resumo Financeiro",
        expand=False
    )
    print(painel)
    volta_para_o_menu()

def resposta_s_n(texto):
    resposta = input(texto).lower()
    if resposta == 'n':
        volta_para_o_menu()
    elif resposta == 's':
        pass
    else:
        erro()