from rich import print

class Produto:
    
    def __init__(self, nome, preco, id, qnt):
        self.nome = nome
        self.preco = preco
        self.id = id
        self.qnt = qnt

    def mudar_preco(self):
        print(f'O atual preço do produto {self.nome} é {self.preco}')
        preco_novo = float(input(f'Qual o preço novo do(a) {self.nome}: '))
        print('O preço foi alterado com sucesso.')

